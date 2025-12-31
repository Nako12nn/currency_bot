import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from app.config import get_settings
from app.services.redis_cache import get_redis
from app.handlers.start_handler import start_handler
from app.handlers.rate_handler import rate_handler
from app.handlers.currencies_handler import currencies_handler
from app.database.init_db import init_db
from app.database.db import close_db


async def on_startup():
    redis = get_redis()
    try:
        await redis.ping()
        print("Redis connected.")
    except Exception as e:
        print("Redis connection failed:", e)


async def main():
    settings = get_settings()

    bot = Bot(token=settings.TELEGRAM_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, Command(commands=["start"]))
    dp.message.register(rate_handler, Command(commands=["rate"]))
    dp.message.register(currencies_handler, Command(commands=["currencies"]))

    print("The bot is starting up...")

    await on_startup()
    await init_db()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await get_redis().aclose()
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())
