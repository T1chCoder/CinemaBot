from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from app import keyboards as kb

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("Hello!")