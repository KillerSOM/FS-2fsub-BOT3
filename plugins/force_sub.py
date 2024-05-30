#telegram user_id: @Shidoteshika1

from bot import Bot
from pyrogram.types import Message
from config import OWNER_ID
from pyrogram import Client, filters
from database.database import add_channel, del_channel, get_all_channels
#FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 , CNAME1, CNAME2, CILINK1, CILINK2= 0, 0, None, None, None, None


@Bot.on_message(filters.command('add_fsub') & filters.private & filters.user(OWNER_ID))
async def add_forcesub(client:Client, message:Message):
    pro = await message.reply("<b><i>Processing....</i></b>")
    check=0
    channel_ids = await get_all_channels()
    fsubs = message.text.split()[1:]
    
    #if not (len(fsubs)==1 and fsubs[0].isdigit() and fsubs[0]=='0'):
    if len(fsubs) !=2:
        await pro.edit("<b>You need to add 2 Channel ID at a time</b>")
        return
    
    for id in fsubs:
        if id.startswith('-') and id[1:].isdigit() and len(id)==14:
            check+=1
        #elif id == '0':
            #check+=2
        else:
            await pro.edit("<b>Invalid channel ID format.</b>")
            return
    
    if check==2:
        if len(channel_ids)>0:
            for id in channel_ids:
                await del_channel(id)
        for id in fsubs:
            await add_channel(int(id))
    
    await pro.edit(f'<b>Force-Sub Channel Added ✅</b>\n<code><blockquote>{" ".join(fsubs)}</blockquote></code>')
    #await update_fsub(1)



@Bot.on_message(filters.command('delall_fsub') & filters.private & filters.user(OWNER_ID))
async def delete_all_forcesub(client:Client, message:Message):
    pro = await message.reply("<b><i>Processing....</i></b>")
    channels = await get_all_channels()
    #global FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1
  
    if channels:
        for id in channels:
            await del_channel(id)
        await pro.edit("<b><blockquote>⛔️ All Available Channel ID are Deleted...</blockquote></b>")
        #FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 = 0, 0
        #await update_fsub(0)
    else:
        await pro.edit("<b><blockquote>⁉️ No Channel ID Available to Delete !</blockquote></b>")
      



@Bot.on_message(filters.command('fsub_chnl_ids') & filters.private & filters.user(OWNER_ID))
async def get_forcesub(client:Client, message: Message):
    pro = await message.reply("<b><i>Processing....</i></b>")
    channels = await get_all_channels()
    
    if channels:
        channel_list = "\n".join([f"{channel}" for channel in channels])
    else:
        channel_list = "❌ No force-sub channels found."
    
    await pro.edit(f"<b><u>📢 FORCE-SUB CHANNEL IDs:</u></b>\n\n<blockquote><code>{channel_list}</code></blockquote>")
   
