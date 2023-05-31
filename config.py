from pyrogram import Client
from asBASE import asJSON

db = asJSON("as.json")
###


SUDORS = [5789819429] # ايديات المطورين
API_ID = 20742090
API_HASH = "4c13d34781a820aa5c4d2e6de8df7122"
TOKEN = "" # التوكن
bot = Client("control",API_ID,API_HASH,bot_token=TOKEN,in_memory=True)
bot_id = TOKEN.split(":")[0]
