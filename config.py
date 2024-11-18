from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
from app import views
import os

load_dotenv()

BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
DB_URL = os.getenv("DB_URL")
MESSAGE_CLEAR = bool(os.getenv("MESSAGE_CLEAR", False)) == True
DB = bool(os.getenv("DB", False)) == True

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher()

engine = create_async_engine(url=DB_URL)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Data:
    page = views.HomeView
    message_clear = MESSAGE_CLEAR
    db = DB
    messages = []
    last_message = []
    echo = True
    blocked_users = []

async def db(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
