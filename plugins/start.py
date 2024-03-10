#(©)CodeXBotz




import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
#from telegram.constants import ParseMode


from bot import Bot
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, HELP_TEXT, START_PIC, LOG_CHNL
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user

ONGOING = "https://telegra.ph/file/c303fe34a28376a6c7bfe.jpg"
GIF = "https://te.legra.ph/file/f3e706834705fa00cd5e2.mp4"


@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    ui = message.from_user.id
    un = message.from_user.username
    um = message.from_user.mention
    #await message.text.forward(chat_id=CHANNEL_ID)
    #forwarded_message = await bot.send_message(CHANNEL_ID, message.text)
    # Add a forward tag to the forwarded message
    await client.send_message(LOG_CHNL, text=f'<b>𝐒𝐓𝐀𝐑𝐓 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃 𝐁𝐘:</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>ᴜsᴇʀ ᴛʏᴘᴇ: Subscriber</b>\n<b>ɪᴅ:</b> <code>{ui}</code>\n<b>ᴜsᴇʀ ɴᴀᴍᴇ: @{un}\nᴍᴇɴᴛɪᴏɴ: {um}</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nBOT:@{client.username}')
    
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Loading...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⛩️ Anime Channel', url = 'https://t.me/BTTH480P'),
                    InlineKeyboardButton('🌐 Chat Group', url = 'https://t.me/BTTH_GROUP')
                ]])
         
        await message.reply_video(
            video= GIF,
            caption = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
        )
        return


@Bot.on_message(filters.command('help') & filters.private)
async def help(client: Client, message: Message):
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Ask your Queries here', url='https://t.me/btth_group')
         ]
               #[ InlineKeyboardButton("🤖 Bot Commands", callback_data = "command"), InlineKeyboardButton("⛔️ Close", callback_data = "close")]
         ])
         
        await message.reply_video(
            video= GIF,
            caption= HELP_TEXT.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            #parse_mode='HTML'#quote = True
        )
        return

"""@Bot.on_message(filters.command('test') & filters.private)
async def test(client: Client, message: Message):
  await message.reply("<blockquote>Testing</blockquote>\n > Quote Test")"""

"""app = Client("my_session")

@Bot.on_message(filters.command('test') & filters.private)
async def test(client: Client, message: Message):
    # Your start message with a block quote
    start_message = 
    > Hello! Welcome to my bot.
    > This is a block quote example.
    > Feel free to explore the features!
    
    await message.reply(start_message, parse_mode="markdown")"""


    
                     #InlineKeyboardButton("🤖", callback_data = "about"),
                     #InlineKeyboardButton("⛔️", callback_data = "close"),
                     #InlineKeyboardButton("❕", callback_data = "help")

"""loading = await message.reply_video(video= "https://te.legra.ph/file/3014bff8535b3c2d216ba.mp4", caption= "<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▱ ▱ ▱ ▱")
        await asyncio.sleep(0.5)
        loading2 = await loading.edit("<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▰ ▱ ▱ ▱")
        await asyncio.sleep(0.5)
        loading3 = await loading2.edit("<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▰ ▰ ▱ ▱")
        await asyncio.sleep(0.5)
        loading4 = await loading3.edit("<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▰ ▰ ▰ ▱")
        await asyncio.sleep(0.5)
        loading5 = await loading4.edit("<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▰ ▰ ▰ ▰")
        await asyncio.sleep(0.5)"""
            
   
#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##

    

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    ui = message.from_user.id
    un = message.from_user.username
    um = message.from_user.mention
    #await message.text.forward(chat_id=CHANNEL_ID)
    #forwarded_message = await bot.send_message(CHANNEL_ID, message.text)
    # Add a forward tag to the forwarded message
    await client.send_message(LOG_CHNL, text=f'<b>𝐒𝐓𝐀𝐑𝐓 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃 𝐁𝐘:</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>ᴜsᴇʀ ᴛʏᴘᴇ: None-Subscriber\n</b><b>ɪᴅ:</b> <code>{ui}</code>\n<b>ᴜsᴇʀ ɴᴀᴍᴇ: @{un}\nᴍᴇɴᴛɪᴏɴ: {um}</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nBOT:@{client.username}')
    
    buttons = [
        [
             InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
             InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸", url=client.invitelink2)    
        ]
    ]
    try:
       buttons.append(
            [
                InlineKeyboardButton(
                    text = '♻️ Try Again',
                    url = f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass
    
    await message.reply_video(
        video ="https://graph.org//file/3b225ba011c151045bcc4.mp4",
        caption = FORCE_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        #quote = True,
        #disable_web_page_preview = True
    )
    
    
@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()
