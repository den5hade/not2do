from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie

from core.config import settings
from api.api_v1.routers import router
from models.user_model import User
from models.progress_model import ProgressModel

# Simple MongoDB connection URL without auth
MONGODB_URL = "mongodb://mongodb:27017/not2do"

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Create MongoDB client
        client = AsyncIOMotorClient(MONGODB_URL)
        # Get database
        db = client.get_database("not2do")
        
        # Initialize beanie with the database instance
        await init_beanie(
            database=db,
            document_models=[
                User,
                ProgressModel,
            ],
        )
        print("Successfully connected to MongoDB")
        yield
        # Close client connection
        client.close()
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Print the error details in the console
    print("Validation Error Occurred:")
    print(f"Request Body: {exc.body}")
    print(f"Error Details: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router, prefix=settings.API_V1_STR)