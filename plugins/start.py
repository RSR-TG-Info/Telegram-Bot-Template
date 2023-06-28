from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def bstart(client, message):
    await client.send_message(chat_id=message.chat.id, text="Start message :)\n\nSource code: https://github.com/RSR-TG-Info/Telegram-Bot-Template", reply_to_message_id=message.id, disable_web_page_preview=True)
    return
