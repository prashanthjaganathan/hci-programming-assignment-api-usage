const express = require('express');
const axios = require('axios');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Serve the main HTML file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Proxy endpoint to communicate with FastAPI backend
app.post('/api/chat', async (req, res) => {
    try {
        const response = await axios.post(`${BACKEND_URL}/chat`, {
            message: req.body.message
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error calling backend API:', error.message);
        res.status(500).json({
            response: 'Sorry, I encountered an error. Please try again.',
            status: 'error'
        });
    }
});

// Proxy endpoint for hello world message
app.post('/api/hello-world', async (req, res) => {
    try {
        const response = await axios.post(`${BACKEND_URL}/hello-world`);
        res.json(response.data);
    } catch (error) {
        console.error('Error calling backend API:', error.message);
        res.status(500).json({
            response: 'Sorry, I encountered an error generating the hello world message.',
            status: 'error'
        });
    }
});

app.listen(PORT, () => {
    console.log(`Frontend server running on http://localhost:${PORT}`);
    console.log(`Backend URL: ${BACKEND_URL}`);
});
