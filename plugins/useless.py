from bot import Bot
import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
#from datetime import datetime
#from helper_func import get_readable_time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

"""@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))"""

@Bot.on_message(filters.command('cmd') & filters.user(ADMINS))
async def bcmd(bot: Bot, message: Message):
    reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❌  𝗗𝗘𝗟𝗘𝗧𝗘", callback_data = "close")
         ]
               #[ InlineKeyboardButton("🤖 Bot Commands", callback_data = "command"), InlineKeyboardButton("⛔️ Close", callback_data = "close")]
         ])
    await message.reply(text="<b>❏ Cᴏᴍᴍᴀɴᴅs ғᴏʀ ʙᴏᴛ Aᴅᴍɪɴs\n\n‣ /batch :</b> create group messages\n\n<b>‣ /genlink :</b> create link for one post\n\n<b>‣ /broadcast :</b> broadcast Message\n\n<b>‣ /info :</b> view bot Statistics + Uptime\n<b>", reply_markup = reply_markup, quote= True)
    
        

@Bot.on_message(filters.private)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)


"""app = Client("my_session")

@Bot.on_message(filters.command('test') & filters.private)
async def test(bot: Bot, message: Message):
    # Your start message with a block quote
    start_message = "> Hello! Welcome to my bot.\n> This is a block quote example.\n> Feel free to explore the features!"
    await message.reply(start_message, parse_mode="markdown")"""
