from functools import lru_cache

from pydantic import BaseSettings, SecretStr


class Config(BaseSettings):
    app_name: str = "MongoDB_API"
    mongo_user: str = None
    mongo_password: SecretStr = None
    mongo_host: str
    mongo_port: int = 27017
    env: str = "dev"

    class Config:
        env_file = ".env"


@lru_cache()
def get_config():
    return Config()
