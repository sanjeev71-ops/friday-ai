from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FRIDAY"
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000
    OLLAMA_BASE_URL: str = "http://127.0.0.1:11434"

    class Config:
        env_file = ".env"


settings = Settings()
