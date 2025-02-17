from typing import Annotated, List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field


class ProgressModel(Document):
    first: List[datetime] = []
    second: List[datetime] = []
    third: List[datetime] = []
    fourth: List[datetime] = []
    user_id: str
    

    @property
    def create(self) -> datetime:
        return self.id.generation_time


    @property
    def get_id(self) -> str:
        return str(self.id)

    
    class Settings:
        name = "progress"
