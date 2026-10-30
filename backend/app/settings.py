from pydantic_settings import BaseSettings

class CoreSettings(BaseSettings):
    DEBUG: bool = False

class Settings(CoreSettings):
    pass

settings = Settings()
