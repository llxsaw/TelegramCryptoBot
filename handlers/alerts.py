import asyncio
from email.message import Message

from aiogram import Router, types
from aiogram.filters import Command
from services.alerts import add_alert, alert_checker
from services.coingecko import get_price
from services.db import get_all_alerts, get_user_alerts

router = Router()


@router.message(Command('alert'))
async def cmd_alert(message: types.Message):
    args = message.text.split()
    if len(args) != 3:
        await message.answer("Использование: /alert <coin_id> <target_price>")
        return

    coin_id = args[1].lower()
    try:
        target_price = float(args[2])
    except ValueError:
        await message.answer("Цена должна быть числом")
        return

    price, _ = await get_price(coin_id)
    if price is None:
        await message.answer("Такой монеты не существует или CoinGecko не вернул данные.")
        return

    await add_alert(message.chat.id, coin_id, target_price)
    await message.answer(f"Оповещение установлено на {coin_id.upper()} при цене {target_price}$")


@router.message(Command("alerts_all"))
async def cmd_alerts_all(message: types.Message):
    alerts = await get_user_alerts(message.chat.id)
    if not alerts:
        await message.answer("У Вас нет активных алертов")
        return

    text = "Ваши активные алерты:\n\n"
    for alert in alerts:
        coin_id, price = alert
        text += f"🪙 {coin_id.upper()} — {price}$\n"
    await message.answer(text)
