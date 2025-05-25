# Pydantic models related to user will be defined here.
# For example, user registration, login, and profile information.
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int # Or str, depending on your DB
    is_active: bool = True

    class Config:
        orm_mode = True # or from_attributes = True for Pydantic v2

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[EmailStr] = None
