from datetime import datetime
from typing import Optional
from models.progress_model import ProgressModel
from fastapi import HTTPException, status


class ProgressService:
    @staticmethod
    async def add_progress(progress: dict) -> ProgressModel:
        progress.date = datetime.strptime(progress.date, "%Y-%m-%d").date()
        print(progress.date)
        print(type(progress.date))
        try:
            progress_in = ProgressModel(**progress.dict())
            await progress_in.insert()
            return progress_in
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to add progress: {str(e)}"
            )


    @staticmethod
    async def get_progress(user_id: str, date: str) -> Optional[ProgressModel]:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        try:
            return await ProgressModel.find_one({
                "user_id": user_id,
                "date": date
            })
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to get progress: {str(e)}"
            )


    @staticmethod
    async def add_to_progress(progress: dict) -> ProgressModel:
        try:
            progress_doc = await ProgressService.get_progress(progress.user_id, progress.date)
            if not progress_doc:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Progress record not found"
                )
            
            update_data = {
                "$push": {
                    field: {"$each": values}
                    for field, values in {
                        "first": progress.first,
                        "second": progress.second,
                        "third": progress.third,
                        "fourth": progress.fourth
                    }.items() if values
                }
            }
            
            await progress_doc.update(update_data)
            return progress_doc
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to update progress: {str(e)}"
            )
