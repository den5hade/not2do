from typing import Annotated, List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field

class User(Document):
    username: Optional[str] = None
    telegram_id: Annotated[str, Indexed(unique=True)] 
    # hashed_password: str
    phone_number: Annotated[str, Indexed(unique=True)] = None
    first_name: str
    last_name: Optional[str] = None
    disabled: Optional[bool] = None
    progress: List[str] = []
    
    def __repr__(self) -> str:
        return f"<User {self.telegram_id}>"

    def __str__(self) -> str:
        return self.telegram_id

    def __hash__(self) -> int:
        return hash(self.telegram_id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.telegram_id == other.telegram_id
        return False
    
    @property
    def create(self) -> datetime:
        return self.id.generation_time
    
    @classmethod
    async def by_email(self, telegram_id: str) -> "User":
        return await self.find_one(self.telegram_id == telegram_id)
    
    class Settings:
        name = "users"