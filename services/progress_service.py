from datetime import datetime

from fastapi import HTTPException, status
from models.progress_model import ProgressModel


class ProgressService:
    @staticmethod
    async def add_progress(progress):
        progress_in = ProgressModel(user_id=progress.user_id,
                                    first=progress.first,
                                    second=progress.second,
                                    third=progress.third,
                                    fourth=progress.fourth,
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
        try:
            if await ProgressService.get_progress(id) is None:
                await ProgressService.add_progress(progress)
                print("message from created")
                return {"message": "daily progress created"}
            else:

                progress_add = await ProgressService.get_progress(id)
                result = await progress_add.update({ "$push": {ProgressModel.first: {"$each": progress.first},
                                                            ProgressModel.second: {"$each": progress.second},
                                                            ProgressModel.third: {"$each": progress.third},
                                                            ProgressModel.fourth: {"$each": progress.fourth},} 
                                                            }
                                                        )
                print("message from added")
                return {"message": "daily progress added"}
        except Exception as e:
            print(e)
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        )
    
    