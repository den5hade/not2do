from typing import Annotated
from fastapi import APIRouter
from core.security import get_current_username
from schemas.progress_schema import Progress
from fastapi import Depends
from services.progress_service import ProgressService


progress_router = APIRouter()


@progress_router.post("/create")
async def add_progress(payload: Progress):
    try:
        if await ProgressService.get_progress(payload["user_id"]) is None:
            print("from adding statement")
            new_data = await ProgressService.add_progress(payload)
            return new_data
    except:
        return {"message": "Today progress already is start"}
        


@progress_router.get("/")
async def get_progress(username: Annotated[str, Depends(get_current_username)]):
    print(username)
    print(type(username))
    today_progress = await ProgressService.get_progress(username)
    # print(today_progress.create)
    # print(type(today_progress.create))
    # print(today_progress.get_id)
    # print(type(today_progress.get_id))
    # can return None if not exist
    return today_progress
