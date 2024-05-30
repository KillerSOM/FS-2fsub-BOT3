# force_sub.py

from config import TG_BOT_TOKEN, APP_ID, API_HASH
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from database.database import add_channel, del_channel, get_all_channels

FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 = 0, 0

@Client.on_message(filters.command('add_fsub') & filters.private & filters.user(OWNER_ID))
async def add_forcesub(client: Client, message: Message):
    check = 0
    channel_ids = await get_all_channels()
    fsubs = message.text.split()[1:]

    if len(fsubs) != 2:
        await message.reply("<b>You need to add 2 Channel IDs at a time</b>")
        return

    for id in fsubs:
        if id.startswith('-') and id[1:].isdigit() and len(id) == 14:
            check += 1
        else:
            await message.reply("<b>Invalid channel ID format.</b>")
            return

    if check == 2:
        if channel_ids:
            for id in channel_ids:
                await del_channel(id)
        for id in fsubs:
            await add_channel(int(id))

        await message.reply(f'<b>Force-Sub Channel Added ✅</b>\n<code><blockquote>{" ".join(fsubs)}</blockquote></code>')

        channels = await get_all_channels()
        global FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1

        if len(channels) == 2:
            FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 = channels

@Client.on_message(filters.command('delall_fsub') & filters.private & filters.user(OWNER_ID))
async def delete_all_forcesub(client: Client, message: Message):
    channels = await get_all_channels()
    global FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1

    if channels:
        for id in channels:
            await del_channel(id)
        await message.reply("<b><blockquote>⛔️ All Available Channel IDs are Deleted...</blockquote></b>")
        FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 = 0, 0
    else:
        await message.reply("<b><blockquote>⁉️ No Channel IDs Available to Delete!</blockquote></b>")

@Client.on_message(filters.command('fsub_chnl_ids') & filters.private & filters.user(OWNER_ID))
async def get_forcesub(client: Client, message: Message):
    channels = await get_all_channels()

    if channels:
        channel_list = "\n".join([f"<code>{channel}</code>" for channel in channels])
    else:
        channel_list = "❌ No force-sub channels found."

    await message.reply(f"<b><u>📢 FORCE-SUB CHANNEL IDs:</u></b>\n\n<blockquote>{channel_list}</blockquote>")


# At the end of force_sub.py
if __name__ == "__main__":
    app = Client("my_bot", bot_token=TG_BOT_TOKEN, api_id=APP_ID, api_hash=API_HASH)
    app.run()

