from typing import List
from datetime import datetime
from beanie import Document


class ProgressModel(Document):
    date: datetime = None  # Remove the default value
    first: List[datetime] = []
    second: List[datetime] = []
    third: List[datetime] = []
    fourth: List[datetime] = []
    user_id: str
    
    def __init__(self, **data):
        # Set the date in constructor if not provided
        if 'date' not in data:
            data['date'] = datetime.now().date()
        super().__init__(**data)

    @property
    def create(self) -> datetime:
        return self.id.generation_time

    @property
    def get_id(self) -> str:
        return str(self.id)
    
    class Settings:
        name = "progress"
