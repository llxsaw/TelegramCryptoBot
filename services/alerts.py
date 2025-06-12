import asyncio
from services.coingecko import get_price
from services.db import remove_alert, get_all_alerts, add_alert_db

alerts = []


async def add_alert(chat_id, coin_id, price):
    await add_alert_db(chat_id, coin_id, price)


async def alert_checker(bot):
    while True:
        alerts = await get_all_alerts()
        for alert in alerts:
            chat_id, coin_id, target_price = alert
            price, _ = await get_price(coin_id)
            if price is None:
                continue

            if price >= target_price:
                await bot.send_message(chat_id, f"{coin_id.upper()} достиг цены {price}$")
                await remove_alert(chat_id, coin_id)
        await asyncio.sleep(30)
