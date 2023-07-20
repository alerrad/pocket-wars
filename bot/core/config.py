from os import environ as env

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN: str = env.get("BOT_TOKEN")

    DB_NAME: str = env.get("DB_NAME")
    DB_HOST: str = env.get("DB_HOST")
    DB_PORT: int = env.get("DB_PORT")
    DB_USERNAME: str = env.get("DB_USERNAME")
    DB_PASSWORD: str = env.get("DB_PASSWORD")

    REDIS_PORT: str = env.get("REDIS_PORT")