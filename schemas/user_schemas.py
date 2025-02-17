from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    telegram_id: str = Field(..., min_length=9, max_length=11, description="user tg")
    first_name: str = Field(..., min_length=5, max_length=50, description="user name")
    phone_number: str = Field(default=None, max_length=10, description="user number")
    

class UserOut(BaseModel):
    username: str | None
    telegram_id: str
    phone_number: str
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool] = False
    

class UserUpdate(BaseModel):
    telegram_id: Optional[str] = None
    username: Optional[str] = None
    phone_number: Optional[str] = None