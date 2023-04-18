from functools import lru_cache

from pydantic import BaseSettings, SecretStr


class Config(BaseSettings):
    app_name: str = "MongoDB API"
    mongo_user: str
    mongo_password: SecretStr
    mongo_host: str
    mongo_port: int

    class Config:
        env_file = ".env"


@lru_cache()
def get_config():
    return Config()
