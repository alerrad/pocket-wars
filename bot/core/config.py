from os import environ as env

from dotenv import load_dotenv
from aiogram.types import BotCommand

load_dotenv()


class Config:
    BOT_TOKEN = env.get("BOT_TOKEN")

    BOT_COMMANDS = [
        BotCommand("warrior :username", "get stats of @username"),
        BotCommand("completed :username", "get list of completed katas of @usename"),
        BotCommand("badge :username", "get rank badge of @username"),
        BotCommand("random_kata", "get any random kata"),
        BotCommand("leaderboard", "get a leaderboard of registered chat members"),
        BotCommand("regme", "add your cw accout for stats"),
        BotCommand("unregme", "remove your cw account from stats"),
    ]

    MYSQL_CONNECTION = ""

    REDIS_PORT = env.get("REDIS_PORT")