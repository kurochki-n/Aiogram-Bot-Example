from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery

from utils import tools


class CallbackAnswerMiddleware(BaseMiddleware):
        
    async def __call__(
        self, 
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]], 
        event: CallbackQuery, 
        data: Dict[str, Any]
    ) -> Any:
        """
        There are cases when Telegram processes a 
        single push of an inline button several times. 
        This middleware prevents this error.
        """
        await event.answer()
        return await handler(event, data)