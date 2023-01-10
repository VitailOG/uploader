from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    ACCESS_ID: str = Field(..., env='ACCESS_ID')
    ACCESS_KEY: str = Field(..., env='ACCESS_KEY')


settings = Settings()
