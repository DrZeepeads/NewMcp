# Pydantic models related to chat will be defined here.
# For example, request and response models for chat messages.
from pydantic import BaseModel
from typing import List, Optional

class Message(BaseModel):
    role: str # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    # session_id: Optional[str] = None # Example for session management

class ChatResponse(BaseModel):
    message: Message
    # session_id: Optional[str] = None # Example for session management
    # citations: Optional[List[dict]] = None # Example for citations
