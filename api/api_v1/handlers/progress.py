from fastapi import APIRouter, Request, HTTPException, status, Depends
from typing import Dict, Any
from schemas.progress_schema import Progress
from services.progress_service import ProgressService
from datetime import datetime


progress_router = APIRouter()


@progress_router.post("/", response_model=str)
async def add_progress(payload: Progress) -> str:
    """Create a new progress entry"""
    progress = await ProgressService.add_progress(payload)
    return progress.get_id


@progress_router.get("/", response_model=bool)
async def get_progress(request: Request) -> bool:
    """Check if progress exists for today"""
    print(f"Request headers: {request.headers}")
    user_id = request.headers.get('id')
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User ID is required"
        )
    
    # Use provided date or today's date

    user_date = request.headers.get('userDate')
    return await ProgressService.get_progress(user_id, user_date) is not None


@progress_router.patch("/", response_model=str)
async def update_progress(payload: Progress) -> str:
    """Update existing progress entry"""
    progress = await ProgressService.add_to_progress(payload)
    return progress.get_id
