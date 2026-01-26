from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any

class TodoCreate(BaseModel):
    item: str

class TodoUpdate(BaseModel):
    item: str
    action: str

class TodoItem(BaseModel):
    status: str
    created_at: str
    updated_at: str

class ApiResponse(BaseModel):
    """Professional API Response format"""
    success: bool
    message: str
    data: Optional[Any] = None
    error: Optional[str] = None


