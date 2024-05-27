#(©)CodeXBotz




import pymongo, os
from config import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

user_data = database['users']
channel_data = database['channels']


async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

# New channel functions
async def channel_exist(channel_id: int):
    found = channel_data.find_one({'_id': channel_id})
    return bool(found)
    
async def add_channel(channel_id: int):
    if not await channel_exist(channel_id) or channel_id==0:
        channel_data.insert_one({'_id': channel_id})
        return

async def del_channel(channel_id: int):
    channel_data.delete_one({'_id': channel_id})
    return

async def get_all_channels():
    channel_docs = channel_data.find()
    channel_ids = [doc['_id'] for doc in channel_docs]
    return channel_ids
