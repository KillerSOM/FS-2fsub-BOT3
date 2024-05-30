from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from database.database import add_channel, del_channel, get_all_channels

FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 = 0, 0

@Bot.on_message(filters.command('test') & filters.private & filters.user(OWNER_ID))
async def add_forcesub(client: Client, message: Message):
  await message.reply("Test Succesfull")
