from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def bstart(client, message):
    await client.send_message(chat_id=message.chat.id, text="start message :)", reply_to_message_id=message.id)
    return
