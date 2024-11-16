from aiogram import Bot, Dispatcher
from app.handlers import router
import asyncio
import logging
import config

async def main():
    bot = Bot(token=config.BOT_API_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    await config.db(config.engine)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Process interrupted, shutting down gracefully.")