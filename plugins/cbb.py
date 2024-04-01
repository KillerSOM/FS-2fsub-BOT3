#(©)Codexbotz

from bot import Bot
from config import CHNL_MSG, CHNL_MSG1
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

SCP = "https://graph.org//file/97dba257afa602043b070.jpg"
SOLO = "https://graph.org//file/e50b4e50421ddaaab858f.jpg"
BTTH = "https://graph.org//file/b07335e8e0e5353cbc784.jpg"

"""@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "chnl1":
        await query.message.edit(
                        #photo = BTTH,
            #disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⬅️ Back", callback_data = "start"),
                        InlineKeyboardButton("⛔️ Close", callback_data = "close")
                    ]])
        )        
"""
#text = f"<b>○ Channel: <a href ='https://t.me/BTTH480P'>Battle Through The Heavens</a>\n\n○ Chat Group: <a href ='https://t.me/Yan_Alliance'>Yan Alliance</a>\n\n○ Owner: @Shidoteshika1\n➖➖➖➖➖➖➖➖➖➖➖➖➖</b>",


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "chnl1":
        await query.message.delete()
        await query.message.reply_photo(
            photo=BTTH,
            #caption=f"<b>○ Channel: <a href='https://t.me/BTTH480P'>Battle Through The Heavens</a>\n\n○ Chat Group: <a href='https://t.me/Yan_Alliance'>Yan Alliance</a>\n\n○ Owner: @Shidoteshika1\n➖➖➖➖➖➖➖➖➖➖➖➖➖</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        #InlineKeyboardButton("⬅️ Back", callback_data="start"),
                        #InlineKeyboardButton("⛔️ Cʟᴏsᴇ ᴛʜɪs Pᴀɢᴇ ⛔️", callback_data="close")
                        InlineKeyboardButton('⛩️ Anime Channel', url = 'https://t.me/BTTH480P'),
                        InlineKeyboardButton('🌐 Chat Group', url = 'https://t.me/Yan_Alliance')
                    ],[
                        InlineKeyboardButton('○ Channel Owner ○', url = 'https://t.me/Shidoteshika1')
                    ]
                ]
            )
        )

    elif data == "chnl2":
           await query.message.delete()
           await query.message.reply_photo(
                        photo = SOLO,
                        #caption = f"<b>○ Channel: <a href ='https://t.me/Solo_Leveling_EngSubb'>Solo Leveling</a>\n\n○ Chat Group: <a href ='https://t.me/Leveling_Group'>Leveling Box</a>\n\n○ Owner: @Shidoteshika1\n➖➖➖➖➖➖➖➖➖➖➖➖➖</b>",
            #disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        #InlineKeyboardButton("⬅️ Back", callback_data = "start"),
                        #InlineKeyboardButton("⛔️ Cʟᴏsᴇ ᴛʜɪs Pᴀɢᴇ ⛔️", callback_data = "close")
                        InlineKeyboardButton('⛩️ Anime Channel', url = 'https://t.me/Solo_Leveling_EngSubb'),
                        InlineKeyboardButton('🌐 Chat Group', url = 'https://t.me/Leveling_Group')
                    ],[
                        InlineKeyboardButton('○ Channel Owner ○', url = 'https://t.me/Shidoteshika1')
                    ]])
        )
    elif data == "chnls":
        await query.message.edit(
                    #photo = SCP,
                    text = f"<b><blockquote>+ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟs ᴛᴏ ᴛʜᴇ Bᴏᴛ +</blockquote>\n\n○ Channel 1: <a href='{client.invitelink}'>Click Here</a>\n○ Channel 2: <a href='{client.invitelink2}'>Click Here</a>",
            #disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
            [
                
                    #InlineKeyboardButton('⛩️ OUR OTHER CHANNELS ⛩️', url='https://t.me/animemoviesr/3171')
                [
                     InlineKeyboardButton('🤖 Dᴇᴠᴇʟᴏᴘᴇʀ', url = 'https://t.me/Shidoteshika1'),
                     InlineKeyboardButton("⛔ Cʟᴏsᴇ", callback_data = "close")
                     #InlineKeyboardButton("Cʜᴀɴɴᴇʟ 𝟷", callback_data = "chnl1"),
                     #InlineKeyboardButton("Cʜᴀɴɴᴇʟ 𝟸", callback_data = "chnl2"),
                     #InlineKeyboardButton("❕", callback_data = "help")
                ]])
        )
    elif data == "command":
           await query.message.edit_text(
                        text = """<b>○ <u>BOT COMMANDS</u> ○

❏ Cᴏᴍᴍᴀɴᴅs ғᴏʀ ʙᴏᴛ Aᴅᴍɪɴs

‣ /start :</b> start the bot or get posts
<b>‣ /batch :</b> create group messages
<b>‣ /genlink :</b> create link for one post
<b>‣ /users :</b> view bot statistics
<b>‣ /broadcast :</b> broadcast Message
<b>‣ /stats :</b> checking your bot uptime

➪ For more Help Contact- <b>@ChatBox480</b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⬅️", callback_data = "hstart"),
                        InlineKeyboardButton("⛔️", callback_data = "close")
                    ]])
        )
    elif data == "hstart":
           await query.message.edit_text(
                        text = """<b>Hello User,

I am a simple file renamer bot that can only store files for a specific channel. You need to join below channels to use me properly.

1. Anime Channel: <a href= 'https://t.me/Animemoviesr'>infinity void ∞</a>
2. Ongoing Channel: <a href= 'https://t.me/Infinity_Ongoing'>∞ ongoing</a></b>

<b>/help</b> - Only this command you can use without joining any channel.

<b>For Contact Admins, Click Below:</b>""",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                 [
               
                    [
                          InlineKeyboardButton('Join Support Group', url='https://t.me/chatbox480')
                    ]
                     #[InlineKeyboardButton("🤖 Bot Commands", callback_data = "command"),InlineKeyboardButton("⛔️ Close", callback_data = "close")]
                    ])
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
                 
