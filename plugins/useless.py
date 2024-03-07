from bot import Bot
import asyncio
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))

@Bot.on_message(filters.command('bcmd') & filters.user(ADMINS))
async def bcmd(bot: Bot, message: Message):
    reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⛔️ Close", callback_data = "close")
         ]
               #[ InlineKeyboardButton("🤖 Bot Commands", callback_data = "command"), InlineKeyboardButton("⛔️ Close", callback_data = "close")]
         ])
    tmp_msg = await message.reply(text="<b>❏ Cᴏᴍᴍᴀɴᴅs ғᴏʀ ʙᴏᴛ Aᴅᴍɪɴs\n\n‣ /start :</b> start the bot or get posts\n<b>‣ /batch :</b> create group messages\n<b>‣ /genlink :</b> create link for one post\n<b>‣ /users :</b> view bot statistics\n<b>‣ /broadcast :</b> broadcast Message\n<b>‣ /stats :</b> checking your bot uptime\n", reply_markup = reply_markup)
    await asyncio.sleep(30)
    await tmp_msg.delete()
    await message.delete()
        

@Bot.on_message(filters.private)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
