#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import asyncio
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1, CHANNEL_ID, PORT, LOG_CHNL, OWNER_ID
from database.database import get_all_channels

async def fetch_fsub():
    channels = await get_all_channels()
    fsub1, fsub2=None, None
    if len(channels)==2:
        fsub1 = channels[0]
        fsub2 = channels[1]
    if len(channels)==1 and channels[0]==0:
        fsub1 = channels[0]
        fsub2 = channels[0]
    return fsub1, fsub2


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
       
        fsub1, fsub2 = await fetch_fsub()
        global FORCE_SUB_CHANNEL;  FORCE_SUB_CHANNEL = FORCE_SUB_CHANNEL if fsub1 is None else fsub1
        global FORCE_SUB_CHANNEL1; FORCE_SUB_CHANNEL1 = FORCE_SUB_CHANNEL1 if fsub2 is None else fsub2 

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                cname = (await self.get_chat(FORCE_SUB_CHANNEL)).title
                
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
    
                self.invitelink = link
                self.name = cname
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("Bot Stopped..")
                sys.exit()

        if FORCE_SUB_CHANNEL1:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL1)).invite_link
                cname = (await self.get_chat(FORCE_SUB_CHANNEL1)).title
                
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL1)).invite_link
    
                self.invitelink2 = link
                self.name2 = cname
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("Bot Stopped..")
                sys.exit()
                
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Testing")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("Bot Stopped..")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!")
        self.LOGGER(__name__).info(f"🇩 🇴 🇳 🇪  ✅")
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

        s_msg = await self.send_message(chat_id = LOG_CHNL, text = f"<b>🤖 <a href='t.me/{self.username}'>Bot</a> Restarted...</b>")
        o_msg = await self.send_message(OWNER_ID, text = f"<b><blockquote>🤖 Bot Restarted succesfully...✅</blockquote></b>")
        await asyncio.sleep(30)
        await s_msg.delete()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
