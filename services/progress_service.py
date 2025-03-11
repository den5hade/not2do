from datetime import datetime

from models.progress_model import ProgressModel


class ProgressService:
    @staticmethod
    async def add_progress(progress):
        progress_in = ProgressModel(**progress.dict())
        await progress_in.insert()
        return progress_in


    @staticmethod
    async def get_progress(id: str):
        today_progress = await ProgressModel.find_one(ProgressModel.user_id == id, ProgressModel.date == datetime.now().date())
        return today_progress
    

    @staticmethod
    async def add_to_progress(id: str, progress: dict):
        progress_add = await ProgressService.get_progress(id)
        await progress_add.update({ "$push": {ProgressModel.first: {"$each": progress.first},
                                                ProgressModel.second: {"$each": progress.second},
                                                ProgressModel.third: {"$each": progress.third},
                                                ProgressModel.fourth: {"$each": progress.fourth},} 
                                                            }
                                                        )
        return progress_add
