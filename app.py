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

MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")

username = urllib.parse.quote_plus(MONGO_INITDB_ROOT_USERNAME)
password = urllib.parse.quote_plus(MONGO_INITDB_ROOT_PASSWORD)


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
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )


@app.get("/items/{user_name}", summary='Get details of currently logged in user', response_model=UserOut)
async def read_item(user_name: str):
    return await UserService.get_user_by_email(user_name)