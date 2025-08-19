from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery


class CallbackAnswerMiddleware(BaseMiddleware):
    
    async def __call__(
        self, 
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]], 
        event: CallbackQuery, 
        data: Dict[str, Any]
    ) -> Any:
        result = await handler(event, data)
        try:
            await event.answer()
        finally:
            return result
