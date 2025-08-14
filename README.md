Module1 Backend
This is the backend service for a bilingual conversational AI assistant, developed for the Cognify-SAI project. The service is built with FastAPI and LangChain and provides a single API endpoint for real-time text chat in both English and Arabic.

Key Features
Real-time Chat Endpoint: A /chat endpoint for sending and receiving messages.

Bilingual Interaction: Automatically detects if the user's message is in English or Arabic and responds in the same language.

Modular Architecture: The code is organized into separate files for routes and services for better scalability and maintenance.

Technology Stack: Built with Python, FastAPI, and LangChain, using OpenAI for the AI model.

Getting Started
Prerequisites
Python 3.10+

pip (Python package installer)

A valid OpenAI API Key

Setup Instructions
Clone the Repository:

git clone https://github.com/HimaShin/cognify-sai-backend.git
cd cognify-sai-backend

Create and Activate a Virtual Environment:

python -m venv .venv
.venv\Scripts\activate

Install Dependencies:

pip install "fastapi[all]" langchain_core langchain_openai python-dotenv

Configure API Key:
Create a file named .env in the root directory and add your OpenAI API key:

OPENAI_API_KEY="your_api_key_here"

Replace your_api_key_here with your actual key.

Run the Server:

uvicorn main:app --reload

The server will be running at http://127.0.0.1:8000.

API Documentation
The interactive API documentation is available at http://127.0.0.1:8000/docs. You can use this to test the /chat endpoint and view the request and response schemas.
