# main.py
# This is the main application file that initializes the FastAPI app and includes the API routes.

import sys
import os

# Get the directory of the current file and add it to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

# Import the API router from your new routes file
from routes import chat_router

# --- API Key Configuration ---
# Load environment variables from .env file
load_dotenv()

# Ensure your OpenAI API key is set as an environment variable
if "OPENAI_API_KEY" not in os.environ:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Cognify-SAI Backend API",
    description="A backend for a bilingual conversational AI assistant.",
)

# Include the API router
app.include_router(chat_router)

# --- How to Run the Server ---
# To run this server, you'll need to set the OPENAI_API_KEY environment variable.
# Then, save the code as `main.py` and run:
# pip install "fastapi[all]" langchain_core langchain_openai python-dotenv
# uvicorn main:app --reload
