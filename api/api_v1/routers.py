from fastapi import APIRouter
from api.api_v1.handlers import unsubscribe, user
from api.api_v1.handlers import progress

router = APIRouter()

router.include_router(user.user_router, prefix='/users', tags=["users"])
router.include_router(progress.progress_router, prefix="/progress", tags=["progress"])
router.include_router(unsubscribe.unsubscribe_router, prefix="/unsubscribe", tags=["unsubscribe"])