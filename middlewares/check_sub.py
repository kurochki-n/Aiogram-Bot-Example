from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from data.config import CHANNEL_ID


class CheckSubscription(BaseMiddleware):
    
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member(CHANNEL_ID, event.from_user.id)
        
        if chat_member.status == "left":
            await event.answer(...)
        else:
            return await handler(event, data)