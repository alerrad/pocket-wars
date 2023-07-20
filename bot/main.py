import asyncio

import aiogram.types as tgTypes
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters import ChatTypeFilter

from .core import bot, logger, dp, UserData
from .handlers import DB_handler, API_handler


@dp.message_handler(state="*", commands=["cancel"])
async def cancel_handler(msg: tgTypes.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is None: return
    logger.info(f"Cancelling state {current_state}")
    
    await msg.reply("Cancelled.")
    await state.finish()

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.all()), commands=["start"])
async def start(msg: tgTypes.Message):
    name = msg.from_user.first_name

    await bot.send_message(
        msg.chat.id,
        f"Hello, {name}!\nI am pocketwars and can help you track & share your progress in codewars, suggest katas & organize leaderboards in group chats!"
    )

## Personal commands

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.all()), commands=["warrior"])
async def get_warrior(msg: tgTypes.Message):
    if len(msg.text.split()) != 2:
        await bot.send_message(
            msg.chat.id,
            "please, use following syntax /warrior @username"
        )
    else:
        ## TODO: check for null & format success data
        warrior = API_handler.get_warrior(msg.text.split()[1])
        await bot.send_message(
            msg.chat.id,
            f"Stats of the following user: {warrior}"
        )

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.all()), commands=["completed"])
async def get_completed(msg: tgTypes.Message):
    if len(msg.text.split()) != 2:
        await bot.send_message(
            msg.chat.id,
            f"Please, use following format /completed @username"
        )
    else:
        completed = API_handler.get_completed()
        ## TODO check for null & format success data

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.all()), commands=["badge"])
async def get_badge(msg: tgTypes.Message):
    username = msg.text.split()[1]
    badgeURL = API_handler.get_badge(username)

    await bot.send_photo(
        msg.chat.id,
        badgeURL
    )

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.PRIVATE), commands=["random_kata"])
async def random_kata(msg: tgTypes.Message):
    await bot.send_message('Command "random_kata" is currently inaccessible because of API v1.\nTry later')


## Group chat commands

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.GROUP), commands=["leaderboard"])
async def leaderboard(msg: tgTypes.Message):
    group_id = msg.chat.id
    ## 1) get all the registered users where groupId = group_id using DB_handler
    ## 2) send leaderboard message if at least 1 user exists, otherwise "No registered users"

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.GROUP), commands=["regme"])
async def regme(msg: tgTypes.Message):
    await UserData.username.set()
    await msg.reply("Enter your codewars username")

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.GROUP), state=UserData.username)
async def process_username(msg: tgTypes.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = msg.text
    
    res = DB_handler.add_user()
    
    await msg.reply(res)
    await state.finish()

@dp.message_handler(ChatTypeFilter(tgTypes.ChatType.GROUP), commands=["unregme"])
async def unregme(msg: tgTypes.Message):
    group_id = msg.chat.id
    user_id = msg.from_user.id
    ## 1) unreg user where groupId = group_id and userId = user_id using DB_handler
    ## 2) send "success" message on success, "no user found" on failure


## Entry point
def start_bot() -> None:
    try:
        logger.info("Bot started!")
        executor.start_polling(dp)
    except Exception as err:
        logger.error(f"Error occured: {err}")
        dp.stop_polling()