# AI Chat Assistant - Hello World Application

A modern web application that demonstrates integration with OpenAI's API to create an interactive AI chat experience. This project showcases a clean, responsive UI with real-time chat functionality.

## 🚀 Features

- **Clean Modern UI**: Inspired by modern AI chat interfaces with a beautiful gradient design
- **Real-time Chat**: Interactive conversation with OpenAI's GPT models
- **Hello World Demo**: Automatic generation of creative "Hello World" messages
- **Quick Actions**: Pre-defined action buttons for common tasks
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **No Authentication Required**: Anyone can use the application immediately

## 🏗️ Architecture

- **Backend**: Python FastAPI server handling API requests
- **Frontend**: Node.js Express server serving static files
- **AI Integration**: OpenAI GPT-3.5-turbo for chat responses
- **Communication**: RESTful API between frontend and backend

## 📁 Project Structure

```
hci-programming-assignment-api-usage/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── env.example         # Environment variables template
├── frontend/
│   ├── server.js           # Node.js Express server
│   ├── package.json        # Node.js dependencies
│   └── public/
│       ├── index.html      # Main HTML file
│       ├── styles.css      # CSS styling
│       └── script.js       # Frontend JavaScript
└── README.md              # This file
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- OpenAI API key

### 1. Clone and Navigate to Project

```bash
cd hci-programming-assignment-api-usage
```

### 2. Backend Setup (FastAPI)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env.example .env
# Edit .env file and add your OpenAI API key:
# OPENAI_API_KEY=your_actual_api_key_here

# Start the backend server
python main.py
```

The backend will be running on `http://localhost:8000`

### 3. Frontend Setup (Node.js)

```bash
# Open a new terminal and navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the frontend server
npm start
```

The frontend will be running on `http://localhost:3000`

### 4. Access the Application

Open your browser and navigate to `http://localhost:3000`

## 🔑 Getting an OpenAI API Key

1. Visit [OpenAI's website](https://openai.com/api/)
2. Sign up for an account
3. Navigate to the API section
4. Create a new API key
5. Copy the key and add it to your `.env` file

## 🎯 How to Use

1. **Start a Conversation**: Type your message in the input box and press Enter or click the send button
2. **Quick Actions**: Use the action buttons below the input for common tasks:
   - Compare: Get help comparing options
   - Troubleshoot: Technical assistance
   - Health: Health and wellness advice
   - Fact Check: Verify information
   - Summarize: Summarize content
3. **New Chat**: Click "New Chat" to start fresh
4. **Hello World**: The app automatically generates a creative "Hello World" message when you first load it

## 🔧 API Endpoints

### Backend (FastAPI - Port 8000)

- `GET /` - Health check
- `GET /health` - Detailed health status
- `POST /chat` - Send a message to AI
- `POST /hello-world` - Generate creative "Hello World" message

### Frontend (Express - Port 3000)

- `GET /` - Main application page
- `POST /api/chat` - Proxy to backend chat endpoint
- `POST /api/hello-world` - Proxy to backend hello-world endpoint


## 🎨 UI Features

- **Modern Design**: Clean, minimalist interface with gradient accents
- **Animated AI Sphere**: Floating 3D-style visual element
- **Responsive Layout**: Adapts to different screen sizes
- **Loading States**: Visual feedback during API calls
- **Message History**: Scrollable chat history
- **Quick Actions**: Pre-defined prompts for common tasks

## 📝 Reflection

### Challenges Faced

1. **API Integration Complexity**: Understanding OpenAI's API structure and managing different response formats proved challenging. I experimented with APIs from Anthropic, Groq, and OpenAI, each with slight variations in their implementation. Ultimately, I found OpenAI's API the most easy due to my prior familiarity with it.

### Key Learnings

1. **API Design**:  Gained hands-on experience designing RESTful APIs with robust error handling and well-structured response formats.
2. **UI/UX Design**: Discovered an effective approach to creating polished user interfaces—rather than relying solely on text prompts, I provided AI with mockup images from Dribbble or Figma. This visual context significantly improved the quality of generated interfaces.
3. **AI Integration**: Developed a solid understanding of how to seamlessly integrate generative AI into full-stack applications, which will be invaluable for our project, ChoreMate.
4. **Idea for ChoreMate**: This assignment helped crystallize the initial design and overall vision for ChoreMate. Browsing through Dribbble and Figma for mockup inspiration gave me a clearer picture of what our final project could become.
