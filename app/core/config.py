from pydantic import Field
from pydantic_settings import BaseSettings

from dotenv import load_dotenv
load_dotenv(".env")  # ✅ 무조건 Settings보다 먼저

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "원 마 솔 Assistant"
    DB_URL: str = Field(..., env="DB_URL")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")  # ← 여기에 추가!
##    MODEL_ENDPOINT: str = Field(..., env="MODEL_ENDPOINT")
##    OCR_ENDPOINT: str   = Field(..., env="OCR_ENDPOINT")

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
