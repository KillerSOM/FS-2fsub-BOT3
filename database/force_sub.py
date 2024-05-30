#telegram user_id: @Shidoteshika1

from config import OWNER_ID
from pyrogram import Client, filters
from database.database import add_channel, del_channel, get_all_channels
FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 = 0, 0


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
    
    channels = await get_all_channels()
    global FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1

    if len(channels)==2:
        FORCE_SUB_CHANNEL = channels[0]
        FORCE_SUB_CHANNEL1 = channels[1]

    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL1 :
        try:
            link = (await client.get_chat(FORCE_SUB_CHANNEL)).invite_link
            cname1 = (await client.get_chat(FORCE_SUB_CHANNEL)).title

            link2 = (await client.get_chat(FORCE_SUB_CHANNEL1)).invite_link
            cname2 = (await client.get_chat(FORCE_SUB_CHANNEL1)).title
                
            if not link:
                await client.export_chat_invite_link(FORCE_SUB_CHANNEL)
                link = (await client.get_chat(FORCE_SUB_CHANNEL)).invite_link
                
            if not link2:
                await client.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                link2 = (await client.get_chat(FORCE_SUB_CHANNEL1)).invite_link

            client.cilink1 = link
            client.cilink2 = link2
            client.cname1 = cname1
            client.cname2 = cname2
                
        except:
            print(f"While(/add_fsub) Can't Export Channel Name and Link..., Please Check If the Bot is admin in the FORCE SUB CHANNELS:\nProvided Force sub Channels:- {FORCE_SUB_CHANNEL}, {FORCE_SUB_CHANNEL1}")
            return



@Bot.on_message(filters.command('delall_fsub') & filters.private & filters.user(OWNER_ID))
async def delete_all_forcesub(client: Client, message: Message):
    channels = await get_all_channels()
    global FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1
  
    if channels:
        for id in channels:
            await del_channel(id)
        await message.reply("<b><blockquote>⛔️ All Available Channel ID are Deleted...</blockquote></b>")
        FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 = 0, 0
    else:
        await message.reply("<b><blockquote>⁉️ No Channel ID Available to Delete !</blockquote></b>")
      



@Bot.on_message(filters.command('fsub_chnl_ids') & filters.private & filters.user(OWNER_ID))
async def get_forcesub(client: Client, message: Message):
    channels = await get_all_channels()
    
    if channels:
        channel_list = "\n".join([f"<code>{channel}</code>" for channel in channels])
    else:
        channel_list = "❌ No force-sub channels found."
    
    await message.reply(f"<b><u>📢 FORCE-SUB CHANNEL IDs:</u></b>\n\n<blockquote>{channel_list}</blockquote>")
    
