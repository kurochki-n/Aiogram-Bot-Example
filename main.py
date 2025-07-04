import os
import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from handlers import setup_routers


os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s",
    handlers=[
        logging.FileHandler("logs/logs.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
    )


async def start_polling() -> None:
    bot = Bot(
        token=config.BOT_TOKEN.get_secret_value(), 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=MemoryStorage())
    
    dp.include_routers(setup_routers())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_polling())
