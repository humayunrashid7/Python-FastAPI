from pydantic import BaseSettings
import os

class AppSettings(BaseSettings):
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str

    class Config:
        env_file = '.env'

settings = AppSettings()