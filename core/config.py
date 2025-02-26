from typing import List

from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    MONGO_INITDB_ROOT_USERNAME: str = config("MONGO_INITDB_ROOT_USERNAME", cast=str)
    MONGO_INITDB_ROOT_PASSWORD: str = config("MONGO_INITDB_ROOT_PASSWORD", cast=str)

    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:3000/",
        "http://127.0.0.1:5500"
    ]
    PROJECT_NAME: str = "not2do"
    
    # Database
    # MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)
    
    class Config:
        case_sensitive = True
        
settings = Settings()
