from typing import Annotated, List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field

def datetime_now() -> datetime:
    return datetime.now().date().isoformat()

class ProgressModel(Document):
    date: datetime = Field(default_factory=datetime_now)
    first: List[datetime] = []
    second: List[datetime] = []
    third: List[datetime] = []
    fourth: List[datetime] = []
    user_id: str
    

    @property
    def create(self) -> datetime:
        return self.id.generation_time

    
    class Settings:
        name = "progress"