from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="AI Chat API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    status: str

@app.get("/")
async def root():
    return {"message": "AI Chat API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message to OpenAI API and return the response
    """
    try:
        # check if the OpenAI API key is configured
        if not openai.api_key:
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        # Create a completion using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Provide creative and engaging responses."},
                {"role": "user", "content": request.message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        # get the response from the OpenAI API
        ai_response = response.choices[0].message.content.strip()
        # return the response to the frontend
        return ChatResponse(
            response=ai_response,
            status="success"
        )
    # if there is an error, return an error message
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.post("/hello-world")
async def hello_world():
    """
    Generate a creative "Hello World" message using OpenAI API
    """
    try:
        # check if the OpenAI API key is configured
        if not openai.api_key:
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")
        
        # generate a creative "Hello World" message using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative AI assistant. Generate an engaging and creative 'Hello World' message that showcases AI capabilities."},
                {"role": "user", "content": "Generate a creative 'Hello World' message that demonstrates the power of AI"}
            ],
            max_tokens=100,
            temperature=0.8
        )
        # get the response from the OpenAI API
        hello_message = response.choices[0].message.content.strip()
        # return the response to the frontend
        return ChatResponse(
            response=hello_message,
            status="success"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating hello world message: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
