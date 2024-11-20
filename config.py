from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()

BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
DB_URL = os.getenv("DB_URL")
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