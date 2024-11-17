from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable
from . import actions

class TestMiddleware(BaseMiddleware):
	async def __call__(self, 
										handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
										event: TelegramObject,
										data: Dict[str, Any]) -> Any:
		result = await handler(event, data)
		return result