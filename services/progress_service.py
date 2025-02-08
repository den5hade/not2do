from datetime import datetime
from typing import Optional
from models.progress_model import ProgressModel


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
    async def get_progress(id: str):
        progress = await ProgressModel.find(ProgressModel.user_id == id, ProgressModel.date == datetime.now().date()).to_list()
        return progress