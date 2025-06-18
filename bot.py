import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import start, top, price, social_links, alerts, menu
from services.db import init_db


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(top.router)
    dp.include_router(price.router)
    dp.include_router(social_links.router)
    dp.include_router(alerts.router)
    dp.include_router(menu.router)

    asyncio.create_task(alerts.alert_checker(bot))

    await dp.start_polling(bot)
    await init_db()

if __name__ == '__main__':
    asyncio.run(main())
