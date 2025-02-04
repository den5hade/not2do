from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    telegram_id: int = Field(...,ge=100000000, le=999999999, description="user tg")
    first_name: str = Field(..., min_length=5, max_length=50, description="user name")
    phone_number: str = Field(default=None, min_length=5, max_length=24, description="user number")
    

class UserOut(BaseModel):
    user_id: UUID
    username: str | None
    telegram_id: int
    phone_number: str
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool] = False
    

class UserUpdate(BaseModel):
    telegram_id: Optional[int] = None
    username: Optional[str] = None
    phone_number: Optional[str] = None