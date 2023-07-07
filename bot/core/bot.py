from aiogram import Bot, Dispatcher
from . import Config


bot = Bot(Config.BOT_TOKEN)
bot.set_my_commands(Config.BOT_COMMANDS)
dp = Dispatcher(bot)
dp.skip_updates()