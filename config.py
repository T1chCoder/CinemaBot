from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from aiogram import Bot, Dispatcher
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

class Data:
    page = views.HomeView
    message_clear = MESSAGE_CLEAR
    db = DB
    messages = []
    last_message = []
    echo = True
    blocked_users = []
    list_items = 10

class CustomError(Exception):
    pass