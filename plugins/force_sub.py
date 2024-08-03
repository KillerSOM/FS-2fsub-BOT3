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
    if not fsubs:
        await pro.edit("<b>You need to add Channel IDs</b>")
        return

    channel_list = ""
    for id in fsubs:
        if id.startswith('-') and id[1:].isdigit() and len(id)==14:
            try:
                link = (await client.get_chat(id)).invite_link
                cname = (await client.get_chat(id)).title

                if not link:
                    await client.export_chat_invite_link(id)
                    link = (await client.get_chat(id)).invite_link
                    
                channel_list += f"<b><blockquote>Name: {cname}\nLink: {link}\nId: <code>{id}</code></blockquote></b>\n"
                check+=1
                
            except:
                channel_list += f"<b><blockquote>Unable to Add Fsub\nId: <code>{id}</code>\n<i>Check the ID properly..</i></blockquote></b>\n"
    
    if check == len(fsubs):
        for id in fsubs:
            await add_channel(int(id))
        await pro.edit(f'<b>Force-Sub Channel Added ✅</b>\n\n{channel_list}')
        
    else:
        await pro.edit(f'<b>Error accured while adding Force-Sub Channels ❌</b>\n\n{channel_list}\n<b><i>Please try again...</i></b>')
    #await update_fsub(1)


@Bot.on_message(filters.command('delall_fsub') & filters.private & filters.user(OWNER_ID))
async def delete_all_forcesub(client:Client, message:Message):
    pro = await message.reply("<b><i>Processing....</i></b>")
    channels = await get_all_channels()
    #global FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1
  
    if channels:
        for id in channels:
            await del_channel(id)
        ids = "\n".join([f"<code>{channel}</code>" for channel in channels])
        await pro.edit(f"<b><blockquote>⛔️ All Available Channel ID are Deleted...</blockquote>\n\n<blockquote>{ids}</blockquote></b>")
        #FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 = 0, 0
        #await update_fsub(0)
    else:
        await pro.edit("<b><blockquote>⁉️ No Channel ID Available to Delete !</blockquote></b>")
      



@Bot.on_message(filters.command('fsub_chnl') & filters.private & filters.user(OWNER_ID))
async def get_forcesub(client:Client, message: Message):
    pro = await message.reply("<b><i>Processing....</i></b>")
    channels = await get_all_channels()
    channel_list = "<b>❌ No force-sub channels found.</b>"
    if channels:
        channel_list = ""
        for chnl in channels:
            try:
                id = int(chnl)
                link = (await client.get_chat(id)).invite_link
                cname = (await client.get_chat(id)).title

                if not link:
                    await client.export_chat_invite_link(id)
                    link = (await client.get_chat(id)).invite_link
                    
                channel_list += f"<b><blockquote>Name: {cname}\nLink: {link}\nId: <code>{id}</code></blockquote></b>\n"
                
            except:
                channel_list += f"<b><blockquote>unable to load other details..\nId: <code>{id}</code></blockquote></b>\n"
                
    await pro.edit(f"<b><u>📢 FORCE-SUB CHANNEL IDs:</u></b>\n\n{channel_list}")
   
