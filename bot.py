import os
from pyrogram import Client, filters
from rsrconfig import Config

app = Client(
    "Tlangvaltea",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=dict(root = "plugins"),
)

app.run()
