from enum import StrEnum

from pydantic_settings import BaseSettings


class Env(StrEnum):
    LOCAL = "local"
    STAGE = "stage"
    PROD = "prod"


class Config(BaseSettings):
    ENV: Env = Env.LOCAL

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "000115as!"
    MYSQL_DB: str = "oz_fastapi"
    MYSQL_CONNECT_TIMEOUT: int = 5
    MYSQL_POOL_MAXSIZE: int = 30
