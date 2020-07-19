from pydantic import BaseSettings


class Settings(BaseSettings):
    AWS_SERVER_PUBLIC_KEY: str
    AWS_SERVER_SECRET_KEY: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')