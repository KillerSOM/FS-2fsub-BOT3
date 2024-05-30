#(©)CodeXBotz

import os
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
#from telegram.constants import ParseMode
from datetime import datetime 

from bot import Bot#, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1
from config import ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, HELP_TEXT, START_PIC, LOG_CHNL, OWNER_ID, CHNL_MSG, FFORCE_SUB_CHANNEL, FFORCE_SUB_CHANNEL1
from helper_func import subscribed, encode, decode, get_messages, get_readable_time
from database.database import add_user, del_user, full_userbase, present_user, add_channel, del_channel, get_all_channels
import subprocess
import sys
from database.database import get_all_channels


@Bot.on_message(filters.command('restart') & filters.private & filters.user(OWNER_ID))
async def restart_bot(client: Client, message: Message):
    print("Restarting bot...")
    msg = await client.send_message(OWNER_ID, text="<b><i><blockquote>⚠️ Bot Stopped, And going to Restart...</blockquote></i></b>")
    await asyncio.sleep(2)  # Wait for 2 seconds before restarting
    await msg.delete()
    args = [sys.executable, "main.py"]  # Adjust this if your start file is named differently
    os.execl(sys.executable, *args)
    # Optionally, you can add cleanup tasks here
    #subprocess.Popen([sys.executable, "main.py"])  # Adjust this if your start file is named differently
    #sys.exit()


ONGOING = "https://graph.org//file/b07335e8e0e5353cbc784.jpg"
GIF = "https://graph.org//file/22abe0fc7ddfd5fadb37e.mp4"
FORCE = "https://graph.org//file/ca724c4356b422f3cb6e6.jpg"
SCP = "https://graph.org//file/97dba257afa602043b070.jpg"
HELP = "https://graph.org//file/10f310dd6a7cb56ad7c0b.jpg"

"""@Bot.on_message(filters.command('add_fsub') & filters.private & filters.user(OWNER_ID))
async def add_forcesub(client: Client, message: Message):
    check, loop=0, 0
    channels = await get_all_channels()
        
    fsubs = message.text.removeprefix('/add_fsub').strip().split()
    if len(fsubs)==2 or len(fsubs)==1:
        if len(channels)==1:
            loop=1
        for id in fsubs:
            if id[0]=='-' and len(id)==14 and id.removeprefix('-').isdigit():
                if len(channels)==2 and len(fsubs)==2:
                    await del_channel(channels[0])
                    await del_channel(channels[1])
                if loop==1:
                    await add_channel(int(id))
                    break
                else:
                   await add_channel(int(id))
            elif len(id)==1 and id[0]=='0':
                if loop==1:
                    await add_channel(0)
                    break
                else:
                    await add_channel(0)
            else:
                check=None
                break
    else:
        check=None
    if check==0:
        await message.reply(f'<b>Force-Sub Channel Added ✅</b>\n<blockquote><code>{" ".join(fsubs)}</code></blockquote>')
        #await restart_bot()
    else:
        await message.reply("<b>INVALID USE OF COMMAND:</b>\n"
                            f"<blockquote><b>➪ Check if the command is empty OR the added ID should be correct (13 digit numbers including '-' or 0 only)</b></blockquote>\n{fsubs}")


@Bot.on_message(filters.command('fsub_chnls') & filters.private & filters.user(OWNER_ID))
async def get_forcesub(client: Client, message: Message):
    fsub=''
    channels = await get_all_channels()
    if len(channels)==2:
        fsub= f'<blockquote><code>{channels[0]}</code></blockquote>\n<blockquote><code>{channels[1]}</code></blockquote>'
    elif len(channels)==1:
        fsub = f'<blockquote><code>{channels[0]}</code></blockquote>'
    else:
        fsub = '<blockquote>DEFAULT</blockquote>'
        
    await message.reply(f"<b><u>FORCE-SUB CHANNEL IDs:</b>\n{fsub}")"""


@Bot.on_message(filters.command('add_fsub') & filters.private & filters.user(OWNER_ID))
async def add_forcesub(client: Client, message: Message):
    check=0
    channel_ids = await get_all_channels()
    fsubs = message.text.split()[1:]
    
    #if not (len(fsubs)==1 and fsubs[0].isdigit() and fsubs[0]=='0'):
    if len(fsubs) > 2 or len(fsubs) < 2:
        await message.reply("<b>You need to add 2 Channel ID at a time</b>")
        return
    
    for id in fsubs:
        if id.startswith('-') and id[1:].isdigit() and len(id)==14:
            check+=1
        #elif id == '0':
            #check+=2
        else:
            await message.reply("<b>Invalid channel ID format.</b>")
            return
    
    if check==2:
        if len(channel_ids)>0:
            for id in channel_ids:
                await del_channel(id)
        for id in fsubs:
            await add_channel(int(id))
    
    await message.reply(f'<b>Force-Sub Channel Added ✅</b>\n<code><blockquote>{" ".join(fsubs)}</blockquote></code>')

@Bot.on_message(filters.command('fsub_chnl_ids') & filters.private & filters.user(OWNER_ID))
async def get_forcesub(client: Client, message: Message):
    channels = await get_all_channels()
    
    if channels:
        channel_list = "\n".join([f"<code>{channel}</code>" for channel in channels])
    else:
        channel_list = "❌ No force-sub channels found."
    
    await message.reply(f"<b><u>📢 FORCE-SUB CHANNEL IDs:</u></b>\n\n<blockquote>{channel_list}</blockquote>")

@Bot.on_message(filters.command('delall_fsub') & filters.private & filters.user(OWNER_ID))
async def delete_all_forcesub(client: Client, message: Message):
    channels = await get_all_channels()
    if channels:
        for id in channels:
            await del_channel(id)
        await message.reply("<b><blockquote>⛔️ All Available Channel ID are Deleted...</blockquote></b>")
    else:
        await message.reply("<b><blockquote>⁉️ No Channel ID Available to Delete !</blockquote></b>")
    

@Bot.on_message(filters.command('start') & (filters.private | filters.group | filters.channel) & subscribed)
async def start_command(client: Client, message: Message):
    #ui = message.from_user.id
    #un = message.from_user.username
    #um = message.from_user.mention
    #await message.text.forward(chat_id=CHANNEL_ID)
    #forwarded_message = await bot.send_message(CHANNEL_ID, message.text)
    # Add a forward tag to the forwarded message
    #if ui in ADMINS :
    #    atype = '<b><blockquote>ᴜsᴇʀ ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ: Admin</blockquote></b>'
    #else :
    #    atype = ''
        
    #await client.send_message(LOG_CHNL, text=f'<b><blockquote>𝐒𝐓𝐀𝐑𝐓 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃 𝐁𝐘:</blockquote></b>\n<b>ɪᴅ:</b> <code>{ui}</code>\n<b>ᴍᴇɴᴛɪᴏɴ: {um}\nᴜsᴇʀ ɴᴀᴍᴇ: @{un}</b>\n<b>ᴜsᴇʀ ᴛʏᴘᴇ: Subscriber ✅</b>\n{atype}', reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Bᴏᴛ-3", url = f"https://t.me/{client.username}"),InlineKeyboardButton("⛔ Cʟᴏsᴇ", callback_data = "close")]]))
     
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
        temp_msg = await message.reply("<b><i>Lᴏᴀᴅɪɴɢ....</i></b>")
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
                    InlineKeyboardButton('🤖 Dev', url = 'https://t.me/Shidoteshika1'),
                    InlineKeyboardButton('⚡ Cʜᴀɴɴᴇʟs', callback_data = 'chnls'),
                    #InlineKeyboardButton("🤖 Aʙᴏᴜᴛ", callback_data = "alt")
                ]])
        #loading = await message.reply("<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▱ ▱ ▱")
        #await asyncio.sleep(0.1)
        #loading2 = await loading.edit("<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▰ ▱ ▱")
        #await asyncio.sleep(0.1)
        #loading3 = await loading2.edit("<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▰ ▰ ▱")
        #await asyncio.sleep(0.1)
        #loading4 = await loading3.edit("<b><i>Lᴏᴀᴅɪɴɢ</i></b> ▰ ▰ ▰")
        #await asyncio.sleep(0.1)
        await message.reply(
            #photo= ONGOING,
            text = START_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            #quote = True
        )
        return


@Bot.on_message(filters.command('help') & filters.private)
async def help(client: Client, message: Message):
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝘚𝘵𝘪𝘭𝘭 𝘩𝘢𝘷𝘦 𝘥𝘰𝘶𝘣𝘵𝘴, 𝘊𝘰𝘯𝘵𝘢𝘤𝘵 𝘈𝘥𝘮𝘪𝘯', url='https://t.me/Shidoteshika1')
         ]
               #[ InlineKeyboardButton("🤖 Bot Commands", callback_data = "command"), InlineKeyboardButton("⛔️ Close", callback_data = "close")]
         ])
         
        await message.reply_photo(
            photo= HELP,
            caption = HELP_TEXT.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            #parse_mode='HTML'#
            #quote = True
        )

        return


@Bot.on_message(filters.command('fsub') & filters.private)
async def check_force_sub(client: Client, message: Message):
    channels = await get_all_channels()
    FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1=0, 0

    if len(channels)==2:
        FORCE_SUB_CHANNEL = channels[0]
        FORCE_SUB_CHANNEL1 = channels[1]

    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 :
        try:
            link = (await client.get_chat(FORCE_SUB_CHANNEL)).invite_link
            cname = (await client.get_chat(FORCE_SUB_CHANNEL)).title

            link2 = (await client.get_chat(FORCE_SUB_CHANNEL1)).invite_link
            cname2 = (await client.get_chat(FORCE_SUB_CHANNEL1)).title
                
            if not link:
                await client.export_chat_invite_link(FORCE_SUB_CHANNEL)
                link = (await client.get_chat(FORCE_SUB_CHANNEL)).invite_link
                
            if not link2:
                await client.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                link2 = (await client.get_chat(FORCE_SUB_CHANNEL1)).invite_link

            ch_n1 = cname
            ch_lnk1 = link
            ch_n2 = cname2
            ch_lnk2 = clink2
                
        except:
            print(f"Can't Export Channel Name and Link..., Please Check If the Bot is admin in the FORCE SUB CHANNELS:\nProvided Force sub Channels:- {FORCE_SUB_CHANNEL}, {FORCE_SUB_CHANNEL1}")
            return    
    else:
        ch_n1 = "No Force-Sub Channel(1) ⛔️"
        ch_lnk1 = f"https://t.me/{client.username}" 
        ch_n2 = "No Force-Sub Channel(2) ⛔️"
        ch_lnk2 = f"https://t.me/{client.username}"         
        

    reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(ch_n1, url=ch_lnk1),
         ],
                [ InlineKeyboardButton(ch_n2, url=ch_lnk2)]#, InlineKeyboardButton("⛔️ Close", callback_data = "close")]
    ])
         
    await message.reply_video(
            video = GIF,
            caption = "<b>CURRENT FORCE-SUB CHANNELS :\n\n<blockquote>Click below buttons to Join</blockquote></b>",
            reply_markup = reply_markup,
            #parse_mode='HTML'#
            #quote = True
    )
    return


@Bot.on_message(filters.command('channel') & filters.private)
async def channel(client: Client, message: Message):
        reply_markup = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton("Cʜᴀɴɴᴇʟ 𝟷", callback_data = "chnl1"),
                     InlineKeyboardButton("Cʜᴀɴɴᴇʟ 𝟸", callback_data = "chnl2")
                     #InlineKeyboardButton('Ask your Queries here', url='https://t.me/Yan_Alliance')
         ]
               #[ InlineKeyboardButton("🤖 Bot Commands", callback_data = "command"), InlineKeyboardButton("⛔️ Close", callback_data = "close")]
         ])
         
        await message.reply_photo(
            photo= SCP,
            caption = CHNL_MSG.format(
                first = message.from_user.first_name,
                last = message.from_user.last_name,
                username = None if not message.from_user.username else '@' + message.from_user.username,
                mention = message.from_user.mention,
                id = message.from_user.id
            ),
            reply_markup = reply_markup,
            #parse_mode='HTML'#
            #quote = True
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
    channels = await get_all_channels()
    FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1=0, 0

    if len(channels)==2:
        FORCE_SUB_CHANNEL = channels[0]
        FORCE_SUB_CHANNEL1 = channels[1]

    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 :
        try:
            link = (await client.get_chat(FORCE_SUB_CHANNEL)).invite_link
            link2 = (await client.get_chat(FORCE_SUB_CHANNEL1)).invite_link
                
            if not link:
                await client.export_chat_invite_link(FORCE_SUB_CHANNEL)
                link = (await client.get_chat(FORCE_SUB_CHANNEL)).invite_link
                
            if not link2:
                await client.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                link2 = (await client.get_chat(FORCE_SUB_CHANNEL1)).invite_link
    
            client.clink = link
            client.clink2 = link2
            
        except:
            print(f"Can't Export Channel Name and Link..., Please Check If the Bot is admin in the FORCE SUB CHANNELS:\nProvided Force sub Channels:- {FORCE_SUB_CHANNEL}, {FORCE_SUB_CHANNEL1}")
            return
            
        buttons = [
            [
                 InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷", url=client.clink),
                 InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸", url=client.clink2)    
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
    
        await message.reply_text(
            #photo = FORCE,
            text = FORCE_MSG.format(
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
    else:
        return
    
    
"""@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")"""

@Bot.on_message(filters.command('info') & filters.private & filters.user(ADMINS))
async def info(client: Bot, message: Message):
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("⛔️  CLOSE  ⛔️", callback_data = "close")]])
    #msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    now = datetime.now()
    delta = now - client.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(f"🚻 : <b>{len(users)} USERS</b>\n\n<b>🤖 UPTIME » {time}</b>", reply_markup = reply_markup, quote= True)
    #await message.reply(BOT_STATS_TEXT.format(uptime=time))

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
