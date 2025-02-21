from typing import List
from datetime import datetime
from beanie import Document


class ProgressModel(Document):
    date: datetime = datetime.now().date()
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
