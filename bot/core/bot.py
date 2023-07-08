from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from . import Config


bot = Bot(Config.BOT_TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

# For step by step registration
class UserData(StatesGroup):
    username = State()