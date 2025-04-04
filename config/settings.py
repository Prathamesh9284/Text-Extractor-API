import os
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Image Text Extraction API"
    
    # API keys
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # CORS settings
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://appt-hr.vercel.app",
        "http://localhost:5173",
        "*"
    ]
    
    class Config:
        env_file = ".env"