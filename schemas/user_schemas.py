from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    telegram_id: str = Field(..., min_length=9, max_length=11, description="user tg")
    first_name: str = Field(..., min_length=2, max_length=50, description="user name")
    last_name: Optional[str] = None
    username: Optional[str] = None
