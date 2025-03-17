from datetime import datetime
from typing import Optional
from models.progress_model import ProgressModel
from fastapi import HTTPException, status


class ProgressService:
    @staticmethod
    def parse_iso_date(date_str: str) -> datetime:
        """Convert ISO date string to datetime object"""
        try:
            # Remove 'Z' and milliseconds for compatibility
            clean_date = date_str.replace('Z', '+00:00')
            return datetime.fromisoformat(clean_date)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid date format. Expected ISO format: {str(e)}"
            )

    @staticmethod
    async def add_progress(progress: dict) -> ProgressModel:
        try:
            # Parse the ISO date string
            date_obj = ProgressService.parse_iso_date(progress.date)
            print(f"Parsed date from POST: {date_obj}")
            print(f"Date type from POST: {type(date_obj)}")
            # Extract just the date part
            progress.date = date_obj.date()
            
            progress_in = ProgressModel(**progress.dict())
            await progress_in.insert()
            return progress_in
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to add progress: {str(e)}"
            )


    @staticmethod
    async def get_progress(user_id: str, date: str):
        try:
            # Parse the ISO date string
            date_obj = ProgressService.parse_iso_date(date)
            # Extract just the date part
            date_only = date_obj.date()
            
            print(f"Parsed date from GET: {date_only}")
            print(f"Date type from GET: {type(date_only)}")
            
            return await ProgressModel.find_one({
                "user_id": user_id,
                "date": date_only
            })
        except HTTPException:
            raise
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
