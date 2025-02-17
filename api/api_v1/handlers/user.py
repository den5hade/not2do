from typing import Annotated
from fastapi import APIRouter, HTTPException, status
from core.security import get_current_username
from schemas.user_schemas import UserAuth, UserOut
from fastapi import Depends
from services.user_services import UserService
import pymongo


user_router = APIRouter()

@user_router.post('/create', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )


@user_router.get("/", summary='Get user', response_model=UserOut)
async def read_item(username: Annotated[str, Depends(get_current_username)]):
    return await UserService.get_user_by_telegram_id(username)
