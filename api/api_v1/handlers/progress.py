from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, status
from core.security import get_current_username
from schemas.progress_schema import Progress
from fastapi import Depends
from services.progress_service import ProgressService
import pymongo


progress_router = APIRouter()


@progress_router.post("/create")
async def add_progress(payload: Progress):
    print(payload)
    new_data = await ProgressService.add_progress(payload) # нужно добавить проверку на наличие
    return new_data


@progress_router.get("/")
async def get_progress(username: Annotated[str, Depends(get_current_username)]):
    today_progress = await ProgressService.get_progress(username)
    # can return None if not exist
    return today_progress
