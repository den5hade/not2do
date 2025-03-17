from datetime import datetime
from typing import List
from pydantic import BaseModel


class Progress(BaseModel):
    date: str
    first: List[datetime] = []
    second: List[datetime] = []
    third: List[datetime] = []
    fourth: List[datetime] = []
    user_id: str
