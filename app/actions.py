from sqlalchemy.future import select
import config
import aiogram
import db as database
import config
import re

async def clear_messages(message):
    if config.Data.messages and config.Data.message_clear:
        messages_to_remove = []
        
        for saved_message in config.Data.messages:
            if saved_message["chat_id"] == message.chat.id:
                try:
                    await config.bot.delete_message(chat_id=saved_message["chat_id"], message_id=saved_message["id"])
                    messages_to_remove.append(saved_message)
                except aiogram.exceptions.TelegramAPIError as e:
                    if "message to delete not found" in str(e):
                        config.Data.messages.remove(saved_message)
                    else:
                        print(f"Error occurred while deleting message: {e}")
                except Exception as e:
                    print(f"Error occurred while deleting message: {e}")
                    break

        for msg in messages_to_remove:
            config.Data.messages.remove(msg)

def sec_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    return f"{int(hours)}:{int(minutes)}:{int(secs)}"

def add_message(message):
    if config.Data.message_clear:
        config.Data.messages.append({"id": message.message_id, "chat_id": message.chat.id})

def text_parse(txt):
    symbols = ["!", ".", ")", "(", ",", "?", "-", "_"]
    text = txt
    
    for symbol in symbols:
        text = re.sub(rf'(?<!\\){re.escape(symbol)}', rf'\\{symbol}', text)
    
    return text

class db:
    @staticmethod
    async def get(model, uuid=None):
        async with database.AsyncSessionLocal() as session:
            try:
                if uuid:
                    result = await session.execute(select(model).filter_by(uuid=uuid))
                    result = result.scalars().first()
                    if not result:
                        raise config.CustomError(f"Record with uuid '{uuid}' not found in the {model.__name__} table.")
                else:
                    result = await session.execute(select(model))
                    result = result.scalars().all()
                return result
            except Exception as e:
                raise config.CustomError(f"An error occurred while fetching data from the database: {e}")
        
    @staticmethod
    async def search(model, field, text):
        async with database.AsyncSessionLocal() as session:
            search_filter = getattr(model, field).ilike(f"%{text}%") 
            result = await session.execute(select(model).filter(search_filter))
            result = result.scalars().all() 

            return result

    @staticmethod
    async def create(model, data):
        if data:
            async with database.AsyncSessionLocal() as session:
                instance = model()
                
                for item in data:
                    if "var" not in item or "val" not in item:
                        raise config.CustomError(f"Missing 'var' or 'val' in data: {item}")

                    try:
                        setattr(instance, item["var"], item["val"])
                    except AttributeError as e:
                        raise config.CustomError(f"Invalid attribute '{item['var']}' for model {model.__name__}: {e}")
                
                try:
                    session.add(instance)
                    await session.commit()  # Ensure the commit is awaited
                except Exception as e:
                    await session.rollback()  # Rollback in case of failure
                    raise config.CustomError(f"Failed to commit to the database: {e}")
        else:
            raise config.CustomError(f"No data provided")
    
    @staticmethod
    async def delete(model, uuid):
        async with database.AsyncSessionLocal() as session:
            try:
                result = await session.execute(select(model).filter_by(uuid=uuid))
                instance = result.scalars().first()  # Fetch the instance by UUID
                if not instance:
                    raise config.CustomError(f"Record with uuid '{uuid}' not found in the {model.__name__} table.")
                
                await session.delete(instance)  # Delete the instance
                await session.commit()  # Commit the transaction
                return f"Record with uuid '{uuid}' has been deleted."
            except Exception as e:
                await session.rollback()  # Rollback in case of failure
                raise config.CustomError(f"An error occurred while deleting the record: {e}")

    @staticmethod
    async def update(model, uuid, data):
        if not data:
            raise config.CustomError(f"No data provided for update.")
        
        async with database.AsyncSessionLocal() as session:
            try:
                result = await session.execute(select(model).filter_by(uuid=uuid))
                instance = result.scalars().first()  # Fetch the instance by UUID
                if not instance:
                    raise config.CustomError(f"Record with uuid '{uuid}' not found in the {model.__name__} table.")

                # Update the instance's attributes
                for item in data:
                    if "var" not in item or "val" not in item:
                        raise config.CustomError(f"Missing 'var' or 'val' in data: {item}")

                    try:
                        setattr(instance, item["var"], item["val"])
                    except AttributeError as e:
                        raise config.CustomError(f"Invalid attribute '{item['var']}' for model {model.__name__}: {e}")

                await session.commit()  # Commit the transaction
                return f"Record with uuid '{uuid}' has been updated."
            except Exception as e:
                await session.rollback()  # Rollback in case of failure
                raise config.CustomError(f"An error occurred while updating the record: {e}")
            
    """ @staticmethod
    async def filter(model, data):
        from sqlalchemy import select, and_

        if not data:
            raise config.CustomError(f"No data provided for update.")

        async with database.AsyncSessionLocal() as session:
            try:
                query = select(model)
                filters = []
                
                for item in data:
                    if "var" not in item or "val" not in item:
                        raise config.CustomError(f"Отсутствуют ключи 'variable' или 'valuable' в данных: {item}")
                    filters.append(getattr(model, item["var"]) == item["val"])

                if filters:
                    query = query.filter(and_(*filters))
                
                result = await session.execute(query)
                items = result.scalars().all()

                return items
            except Exception as e:
                await session.rollback()  # Rollback in case of failure
                raise config.CustomError(f"An error occurred while filtering the record: {e}")"""