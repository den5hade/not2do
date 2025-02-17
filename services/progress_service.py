from datetime import datetime
from typing import Optional
from models.progress_model import ProgressModel
from schemas.progress_schema import ProgressUpdate
from beanie.odm.operators.update.array import Push


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
        # progress = await ProgressModel.find_one(ProgressModel.user_id == id)
        today_progress = await ProgressModel.find_one(ProgressModel.user_id == id, ProgressModel.date == datetime.now().date())
        return today_progress
    

    @staticmethod
    async def add_to_progress(id: str, progress: dict):
        progress_add = await ProgressModel.find_one(ProgressModel.user_id == id, ProgressModel.date == datetime.now().date())
        print(len(progress_add.first))
        result = await progress_add.update({ "$push": {ProgressModel.first: {"$each": progress.first},
                                                    ProgressModel.second: {"$each": progress.second},
                                                    ProgressModel.third: {"$each": progress.third},
                                                    ProgressModel.fourth: {"$each": progress.fourth},} 
                                                    }
                                                )

        print(len(result.first))
        return {"message": "success"}
    
    