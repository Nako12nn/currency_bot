from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    TELEGRAM_TOKEN: str 
    redis_url: str 
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
#"redis://localhost:6379"