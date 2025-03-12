from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: list = [
        "http://127.0.0.1:5500",
    ]
    PROJECT_NAME: str = "not2do"
    
    class Config:
        case_sensitive = True
        
settings = Settings()
