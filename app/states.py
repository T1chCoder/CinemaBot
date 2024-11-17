from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from handlers import router
from . import templates


class SearchStateView(templates.StateView):
    text = "Привет"
