from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from app import keyboards as kb, states as st
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("Hello!")