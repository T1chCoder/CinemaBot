from aiogram import Bot
from app.handlers import router, register_views
from sqlalchemy.exc import OperationalError
import config
import asyncio
import logging
import db

async def on_start(bot: Bot):
    await bot.delete_webhook()
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url:
        logging.info("Webhook still exists, trying again...")
        await bot.delete_webhook()
    else:
        logging.info("Webhook deleted successfully")


async def init_db():
    try:
        async with db.engine.begin() as conn:
            await conn.run_sync(db.Base.metadata.create_all)
        print("INFO:sqlalchemy.engine.Engine:Database connected successfully")
    except OperationalError as e:
        print("INFO:sqlalchemy.engine.Engine:Error occured while connecting to Database: ", e)

async def main():
    await init_db()
    await register_views(router)
    config.dp.include_router(router)
    await on_start(config.bot)
    await config.dp.start_polling(config.bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Process interrupted, shutting down gracefully")