import os
from dotenv import load_dotenv
from pydantic import BaseSettings, validator

from app.api.models.environment_model import EnvironmentModel


class Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    recaptcha_secret_key: str = os.getenv("RECAPTCHA_SECRET_KEY")
    environment: EnvironmentModel = os.getenv("ENVIRONMENT")

    class Config:
        env_file = ".env"


settings = Settings()
