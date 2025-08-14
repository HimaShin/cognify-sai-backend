# routes/chat.py
# This file defines the API endpoint and handles the request/response logic.

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import Optional

# Import the chatbot service to handle the core logic
from services import chatbot_service

# Define the API router
chat_router = APIRouter()

# Pydantic models for API requests and responses
class ChatRequest(BaseModel):
    user_message: str
    session_id: Optional[str] = "default"

class ChatResponse(BaseModel):
    ai_response: str
    language: str

@chat_router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Main chat endpoint that receives a user message and returns an AI response.
    It uses the chatbot service to handle the core logic.
    """
    try:
        # Call the chatbot service to get the response
        response = await chatbot_service.get_ai_response(
            user_message=request.user_message,
            session_id=request.session_id
        )
        return ChatResponse(ai_response=response["ai_response"], language=response["language"])
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal server error while processing the chat request.")

