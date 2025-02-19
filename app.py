from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie
from dotenv import load_dotenv
import urllib

from api.api_v1.routers import router
from models.user_model import User
from models.progress_model import ProgressModel


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
            ProgressModel,
        ],
    )
    yield


app = FastAPI(title="not2do",
              lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://127.0.0.1:5500",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)