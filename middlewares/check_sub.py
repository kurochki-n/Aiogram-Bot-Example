from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from config_reader import config


class CheckSubscriptionMiddleware(BaseMiddleware):
    
    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member(config.CHANNEL_ID.get_secret_value(), event.from_user.id)
        
        if chat_member.status == "left":
            # executed if the user is not subscribed to the channel
            await event.answer(...)
        else:
            return await handler(event, data)