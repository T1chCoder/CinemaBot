import config

async def clear_messages():
    if config.Data.messages and config.Data.message_clear:
        for saved_message in config.Data.messages:
            try:
                await config.bot.delete_message(chat_id=saved_message["chat_id"], message_id=saved_message["id"])
            except:
                break
        config.Data.messages.clear()

def add_message(message):
    if config.Data.message_clear:
        config.Data.messages.append({"id": message.message_id, "chat_id": message.chat.id})