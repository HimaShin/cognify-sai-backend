# services/chatbot_service.py
# This file contains the core chatbot functionality, including LangChain and language detection.

import os
import re
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

# In-memory chat history (for demonstration)
chat_history = {}

def is_arabic(text: str) -> bool:
    """Detects if a string contains Arabic characters."""
    arabic_regex = re.compile(r"[\u0600-\u06FF]")
    return bool(arabic_regex.search(text))

def get_bilingual_prompt_template(language: str) -> ChatPromptTemplate:
    """Returns a bilingual prompt template based on the detected language."""
    if language == 'arabic':
        return ChatPromptTemplate.from_messages([
            ("system", "أنت مساعد ذكاء اصطناعي ثنائي اللغة مصمم لتقديم إجابات دقيقة ومفصلة. حافظ على الرد باللغة العربية."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ])
    else:
        return ChatPromptTemplate.from_messages([
            ("system", "You are a bilingual AI assistant designed to provide accurate and detailed answers. Always respond in English."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ])

async def get_ai_response(user_message: str, session_id: str):
    """
    Handles the core logic for getting an AI response.
    This function detects the language and uses LangChain to get a response.
    """
    # Initialize session chat history if it doesn't exist
    if session_id not in chat_history:
        chat_history[session_id] = []

    language = "arabic" if is_arabic(user_message) else "english"
    prompt_template = get_bilingual_prompt_template(language)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = prompt_template | llm

    response = await chain.ainvoke({
        "input": user_message,
        "chat_history": chat_history[session_id]
    })
    
    ai_response = response.content

    # Update chat history for the specific session
    chat_history[session_id].append(HumanMessage(content=user_message))
    chat_history[session_id].append(AIMessage(content=ai_response))

    return {"ai_response": ai_response, "language": language}
