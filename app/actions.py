import config
import aiogram

async def clear_messages(message):
    if config.Data.messages and config.Data.message_clear:
        messages_to_remove = []
        
        for saved_message in config.Data.messages:
            if saved_message["chat_id"] == message.chat.id:
                try:
                    await config.bot.delete_message(chat_id=saved_message["chat_id"], message_id=saved_message["id"])
                    messages_to_remove.append(saved_message)
                except aiogram.exceptions.MessageNotFound:
                    print(f"Message {saved_message['id']} not found.")
                except Exception as e:
                    print(f"Error occurred while deleting message: {e}")
                    break

        for msg in messages_to_remove:
            config.Data.messages.remove(msg)

def add_message(message):
    if config.Data.message_clear:
        config.Data.messages.append({"id": message.message_id, "chat_id": message.chat.id})