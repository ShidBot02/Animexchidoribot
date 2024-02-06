from bot import Bot
from pyrogram.types import Message
from pyrogram import Client, filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT, HELP_TEXT, TUTO_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Client.on_message(filters.command('help'))
async def help(client, message):
   await message.reply(HELP_TEXT)

@Client.on_message(filters.command('tutorial'))
async def tutorial(client, message):
    await message.reply(TUTO_TEXT)
