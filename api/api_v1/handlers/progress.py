from typing import Annotated
from fastapi import APIRouter, Request
from core.security import get_current_username
from fastapi import Depends
from schemas.progress_schema import Progress
from services.progress_service import ProgressService


progress_router = APIRouter()


@progress_router.post("/")
async def add_progress(payload: Progress):
    new_data = await ProgressService.add_progress(payload)
    return new_data.get_id
        


@progress_router.get("/")
async def get_progress(request: Request):
    username = request.headers.get('id')
    print(username)
    print(type(username))
    today_progress = await ProgressService.get_progress(username)
    print(f"from GET rout: {today_progress}")
    if today_progress is not None:
        return True
    else:
        return False


@progress_router.patch("/")
async def add_progress(payload: Progress):
    today_progress = await ProgressService.add_to_progress(progress=payload)
    return today_progress.get_id
