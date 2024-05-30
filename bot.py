# bot.py

from aiohttp import web
from plugins import web_server

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, CHANNEL_ID, PORT, LOG_CHNL, OWNER_ID
from force_sub import add_forcesub, delete_all_forcesub, get_forcesub

class Bot(Client):
    def __init__(self, force_sub_channel=None, force_sub_channel1=None):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins=dict(root="plugins"),
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.force_sub_channel = force_sub_channel
        self.force_sub_channel1 = force_sub_channel1

    async def on_connect(self, client, userdata):
        await client.send_message(chat_id=LOG_CHNL, text=f"<b>🤖 Bot connected to Pyrogram...</b>")

    async def on_disconnect(self, client, userdata):
        await client.send_message(chat_id=LOG_CHNL, text=f"<b>🤖 Bot disconnected from Pyrogram...</b>")

    async def on_message(self, message: Message):
        pass

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if self.force_sub_channel:
            try:
                link = (await self.get_chat(self.force_sub_channel)).invite_link

                if not link:
                    await self.export_chat_invite_link(self.force_sub_channel)
                    link = (await self.get_chat(self.force_sub_channel)).invite_link

                self.invitelink = link

            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't export invite link from force sub channel!")
                self.LOGGER(__name__).warning(f"Please double check the force_sub_channel value and make sure bot is admin in channel with invite users via link permission, current force sub channel value: {self.force_sub_channel}")
                self.LOGGER(__name__).info("Bot stopped..")
                sys.exit()

        if self.force_sub_channel1:
            try:
                link = (await self.get_chat(self.force_sub_channel1)).invite_link

                if not link:
                    await self.export_chat_invite_link(self.force_sub_channel1)
                    link = (await self.get_chat(self.force_sub_channel1)).invite_link

                self.invitelink2 = link

            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't export invite link from force sub channel!")
                self.LOGGER(__name__).warning(f"Please double check the force_sub_channel1 value and make sure bot is admin in channel with invite users via link permission, current force sub channel value: {self.force_sub_channel1}")
                self.LOGGER(__name__).info("Bot stopped..")
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Testing")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make sure bot is admin in DB channel, and double check the CHANNEL_ID value, current value {CHANNEL_ID}")
            self.LOGGER(__name__).info("Bot stopped..")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot running..!")
        self.LOGGER(__name__).info(f"🇩 🇴 🇳 🇪  ✅")
        self.username = usr_bot_me.username

        # Web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

        s_msg = await self.send_message(chat_id=LOG_CHNL, text=f"<b>🤖 <a href='t.me/{self.username}'>Bot</a> restarted...</b>")
        o_msg = await self.send_message(OWNER_ID, text=f"<b><blockquote>🤖 Bot restarted successfully...✅</blockquote></b>")
        await asyncio.sleep(30)
        await s_msg.delete()

    def run(self):
        asyncio.get_event_loop().run_until_complete(self.start())
        asyncio.get_event_loop().run_forever()
