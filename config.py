#(©)CodeXBotz

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22980101"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
#log channel
LOG_CHNL = int(os.environ.get("LOG_CHNL", "0")) #not necessary 

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FFORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FFORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start pic
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/d48e6d30e443dcae118b8.jpg")

#start message
START_MSG = os.environ.get("START_MSG", "<b>🍁 Hᴇʏ, {mention} ~\n\n<blockquote>𝘪 𝘢𝘮 𝘢 𝘧𝘪𝘭𝘦 𝘴𝘵𝘰𝘳𝘦 𝘣𝘰𝘵.\n𝘖𝘯𝘭𝘺 𝘧𝘰𝘳 𝘈𝘯𝘪𝘮𝘦 𝘳𝘦𝘭𝘢𝘵𝘦𝘥 𝘴𝘵𝘶𝘧𝘧𝘴</blockquote></b>")#\n<blockquote>🧑‍💻 Developer: @Shidoteshika1</blockquote>

#channel start message
CHNL_MSG = os.environ.get("CHNL_MSG", "<b>🍁 Hᴇʏ, {mention} ~\n\nWellcome to this page. Here you will redirect to my connected channels.\n\nClick Below buttons for redirect My Channels.</b>")

#channel start message
CHNL_MSG1 = os.environ.get("CHNL_MSG1", "<b>🍁 Hᴇᴇʏ ~\n\nWellcome to this page. Here you will redirect to my connected channels.\n\nClick Below buttons for redirect My Channels.</b>")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>⚠️ Hᴇʏ, {mention} ×\n\nJoin my Channels first to receive files or initiate message\n\n❗Facing problems, use: /help</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>I am only file store bot\n\nFor More Info Click: /start</b>\n"

HELP_TEXT = "<b>🍁 Hᴇʟʟᴏ {mention} ~\n\n  I am a file supplier bot and meant to provides Files from Specified Channels. You need to Join Mentioned Channels to get files or Initiate Messages...\n\n/help -</b> Oᴘᴇɴ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ !<b>\n/fsub -</b> Cʜᴇᴄᴋ ʙᴏᴛ-ᴄᴏɴɴᴇᴄᴛᴇᴅ/ғᴏʀᴄᴇ-sᴜʙ ᴄʜᴀɴɴᴇʟs\n<blockquote>You can use above commands without joining force-sub Channels</blockquote>\n"

ADMINS.append(OWNER_ID)
#ADMINS.append(1536699044)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
