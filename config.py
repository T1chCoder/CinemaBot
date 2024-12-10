from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()

BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
DB_NAME = str(os.getenv("DB_NAME"))
DB_USER = str(os.getenv("DB_USER"))
DB_PASSWORD = str(os.getenv("DB_PASSWORD"))
DB_HOST = str(os.getenv("DB_HOST"))
DB_PORT = str(os.getenv("DB_PORT"))
DB_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
MESSAGE_CLEAR = eval(os.getenv("MESSAGE_CLEAR", False)) == True

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher()

class Data:
    from app import views
    
    page = views.HomeView
    message_clear = MESSAGE_CLEAR
    messages = []
    last_message = []
    echo = True
    blocked_users = []
    list_items = 10

class CustomError(Exception):
    pass