from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    telegram_id: int = Field(..., description="user tg")
    username: str = Field(..., min_length=5, max_length=50, description="user username")
    phone_number: str = Field(..., min_length=5, max_length=24, description="user number", default=None)
    

class UserOut(BaseModel):
    user_id: UUID
    username: str
    telegram_id: int
    phone_number: str
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool] = False
    

class UserUpdate(BaseModel):
    telegram_id: Optional[int] = None
    username: Optional[str] = None
    phone_number: Optional[str] = None