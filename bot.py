from pyrogram import Client
from rsrconfig import Config

app = Client(
    "Test Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=dict(root = "plugins"),
)

app.run()
