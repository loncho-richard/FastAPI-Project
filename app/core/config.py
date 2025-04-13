from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #DATABASE_URL: str = "postgresql+psycopg://user:pass@localhost/dbname"
    DATABASE_URL: str = "sqlite:///database.db"
    SECRET_KEY: str = "a5a7cdcf2f97ece4e5f05b782fb947faac18b3210d8186b682bd3f1b45419548"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    CORS_ORIGINS: list[str] = ["*"]

    model_config = SettingsConfigDict(
        env_file = ".env",
        extra="ignore"
    )
        

settings = Settings()