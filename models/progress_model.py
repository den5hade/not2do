from typing import List
from datetime import datetime
from beanie import Document, Indexed
from pydantic import Field


class ProgressModel(Document):
    date: datetime
    first: List[datetime] = Field(default_factory=list)
    second: List[datetime] = Field(default_factory=list)
    third: List[datetime] = Field(default_factory=list)
    fourth: List[datetime] = Field(default_factory=list)
    user_id: str = Indexed()  # Correct syntax for indexed field
    
    @property
    def create_time(self) -> datetime:  # Renamed for clarity
        return self.id.generation_time

    @property
    def get_id(self) -> str:
        return str(self.id)
    
    class Settings:
        name = "progress"
        use_state_management = True  # Enable state management for better consistency
