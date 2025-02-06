from datetime import datetime
from typing import Optional
from models.progress_model import ProgressModel


def datetime_now() -> datetime:
    return datetime.now().date().isoformat()


class ProgressService:
    @staticmethod
    async def add_progress(progress):
        progress_in = ProgressModel(
                first=progress.first,
                second=progress.second,
                third=progress.third,
                fourth=progress.fourth,
                user_id=progress.user_id
            )
        await progress_in.insert()
        return progress_in

    
    

    @staticmethod
    async def get_progress(date: datetime = datetime_now()):
        progress = await ProgressModel.find_one(ProgressModel.date == date)
        return progress