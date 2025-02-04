from contextlib import asynccontextmanager
import os
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from dotenv import load_dotenv
import urllib

import pymongo

from models.user_model import User
from services.user_services import UserService
from schemas.user_schemas import UserAuth, UserOut, UserUpdate


load_dotenv()

username = urllib.parse.quote_plus(os.getenv("MONGO_INITDB_ROOT_USERNAME"))
password = urllib.parse.quote_plus(os.getenv("MONGO_INITDB_ROOT_PASSWORD"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(f"mongodb://{username}:{password}@localhost:27016/not2do?authSource=admin&retryWrites=true&w=majority")
    db = client['not2do']
    await init_beanie(
        database=db,  
        document_models=[
            User,  
        ],
    )
    yield


app = FastAPI(title="not2do",
              lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/create', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth = Depends()):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )


@app.get("/items/{telegram_id}", summary='Get details of currently logged in user', response_model=UserOut)
async def read_item(telegram_id: int):
    return await UserService.get_user_by_telegram_id(telegram_id)