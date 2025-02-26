from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie
import urllib

from core.config import settings
from api.api_v1.routers import router
from models.user_model import User
from models.progress_model import ProgressModel


username = urllib.parse.quote_plus(settings.MONGO_INITDB_ROOT_USERNAME)
# username = settings.MONGO_INITDB_ROOT_USERNAME

password = urllib.parse.quote_plus(settings.MONGO_INITDB_ROOT_PASSWORD)
# password = settings.MONGO_INITDB_ROOT_PASSWORD


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


app = FastAPI(title=settings.PROJECT_NAME,
              openapi_url=f"{settings.API_V1_STR}/openapi.json",
              lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix=settings.API_V1_STR)