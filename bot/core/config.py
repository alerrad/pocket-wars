from os import environ as env

from dotenv import load_dotenv
from aiogram.types import BotCommand

load_dotenv()


class Config:
    BOT_TOKEN = env.get("BOT_TOKEN")

    MYSQL_CONNECTION = ""

    REDIS_PORT = env.get("REDIS_PORT")