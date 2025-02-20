from typing import Annotated
from fastapi import APIRouter
from core.security import get_current_username
from fastapi import Depends
from schemas.progress_schema import Progress
from services.progress_service import ProgressService


progress_router = APIRouter()


@progress_router.post("/create")
async def add_progress(username: Annotated[str, Depends(get_current_username)], payload: Progress):
    try:
        if await ProgressService.get_progress(username) is None:
            print("from adding statement")
            new_data = await ProgressService.add_progress(payload)
            return new_data
        else:
            return {"message": "Today progress already is start"}
    except:
        print("from exception")
        return {"message": "Today progress already is start"}
        


@progress_router.get("/")
async def get_progress(username: Annotated[str, Depends(get_current_username)]):
    today_progress = await ProgressService.get_progress(username)
    return today_progress


@progress_router.patch("/")
async def add_progress(username: Annotated[str, Depends(get_current_username)], payload: Progress):
    today_progress = await ProgressService.add_to_progress(id=username, progress=payload)
    return today_progress