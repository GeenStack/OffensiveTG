import os
from dotenv import load_dotenv
from telethon import TelegramClient

def getClient():
    load_dotenv()
    API_ID = os.getenv("TG_API_ID")
    API_HASH = os.getenv("TG_API_HASH")
    client = TelegramClient(session='otg_session', api_hash=API_HASH, api_id=API_ID)
    client.start()
    return client