from aiogram import Router, types
from services.coingecko import get_price
from services.db import get_user_alerts

router = Router()

@router.message(lambda m: m.text == "📈 Курсы валют")
async def show_prices(message: types.Message):
    btc, _ = await get_price('bitcoin')
    eth, _ = await get_price('ethereum')
    await message.answer(f"📈 BTC: {btc}$\n📈 ETH: {eth}$")


@router.message(lambda m: m.text == '🛎 Мои алерты')
async def show_alerts(message: types.Message):
    alerts = await get_user_alerts(message.chat.id)
    if not alerts:
        await message.answer("У Вас нет активных алертов")
        return
    text = "🔔 Ваши алерты:\n\n"
    for alert_id, coin_id, price in alerts:
        text += f"🪙 {coin_id.upper()} — {price}$ (ID: {alert_id})\n"
    await message.answer(text)


@router.message(lambda m: m.text == '➕ Добавить алерт')
async def add_alert(message: types.Message):
    await message.answer("✍ Введите команду:\n`/alert <coin_id> <target_price>`\n\nПример: `/alert btc 65000`",
                         parse_mode="Markdown")

