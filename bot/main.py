import aiogram.types as tgTypes
from core import bot, logger, dp


@dp.message_handler(commands=["start"])
async def start(msg: tgTypes.Message):
    name = msg.from_user.first_name

    await bot.send_message(
        msg.chat.id,
        f"Hello, {name}!\nI can help you track & share your progress in codewars, suggest katas & organize leaderboards in group chats!"
    )

## Personal commands

@dp.message_handler(commands=["warrior"])
async def get_warrior(msg: tgTypes.Message):
    pass

@dp.message_handler(commands=["completed"])
async def get_completed(msg: tgTypes.Message):
    pass

@dp.message_handler(commands=["badge"])
async def get_badge(msg: tgTypes.Message):
    pass

@dp.message_handler(commands=["random_kata"])
async def random_kata(msg: tgTypes.Message):
    pass


## Group chat commands

@dp.message_handler(commands=["leaderboard"])
async def leaderboard(msg: tgTypes.Message):
    pass



## Entry point

def start_bot() -> None:
    try:
        dp.start_polling()
        logger.info("Bot started!")
    except Exception as err:
        logger.error(f"Error occured: {err}")
        dp.stop_polling()