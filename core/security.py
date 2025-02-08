import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from services.user_services import UserService


security = HTTPBasic()


async def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    user = await UserService.get_user_by_telegram_id(int(credentials.password))

    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = user.first_name.encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = str(user.telegram_id).encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return str(user.telegram_id)
