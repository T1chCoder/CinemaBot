from aiogram import Bot, Dispatcher
from aiogram import Router
from app.handlers import router, register_views
from aiogram.filters import Command
from aiogram.types import Message
import config
import asyncio
import logging

async def on_start(bot: Bot):
    await bot.delete_webhook()
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url:
        logging.info("Webhook still exists, trying again...")
        await bot.delete_webhook()
    else:
        logging.info("Webhook deleted successfully")

async def main():
    await register_views(router)
    config.dp.include_router(router)
    await on_start(config.bot)
    await config.dp.start_polling(config.bot)
    if config.Data.db:
        await config.db(config.engine)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Process interrupted, shutting down gracefully")