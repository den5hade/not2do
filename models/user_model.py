from typing import Annotated, Any, List, Optional
from datetime import datetime
from beanie import Document, Indexed

class User(Document):
    username: Optional[str] = None
    telegram_id: Annotated[str, Indexed(unique=True)]
    first_name: str
    last_name: Optional[str] = None
    disabled: Optional[bool] = None
    
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
    
    class Settings:
        name = "users"