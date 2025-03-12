from fastapi import APIRouter, HTTPException, Request, status
from schemas.user_schemas import UserAuth
from services.user_services import UserService
import pymongo


user_router = APIRouter()


@user_router.get("/", summary='Get user')
async def get_user(request: Request):
    """
    Get user by Telegram ID from request headers.
    
    Args:
        request (Request): FastAPI request object containing headers
        
    Returns:
        User | False: User object if found, False if user doesn't exist
        
    Note:
        Expects 'id' header containing user's Telegram ID
        No authentication required for this endpoint
    """
    telegram_id = request.headers.get('id')
    user = await UserService.get_user_by_telegram_id(telegram_id)
    return False if user is None else user


@user_router.post("/", summary='Get user')
async def read_item(data: UserAuth):
    print(data)
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )
