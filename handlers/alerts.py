import asyncio
from email.message import Message

from aiogram import Router, types
from aiogram.filters import Command
from services.alerts import add_alert, alert_checker
from services.coingecko import get_price
from services.db import get_all_alerts, get_user_alerts, remove_alert
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

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

    for alert in alerts:
        alert_id, coin_id, price = alert
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='❌ Удалить', callback_data=f"delete_alert:{alert_id}")],
        ])
        await message.answer(
            f"🪙 {coin_id.upper()} — {price}$\nID: {alert_id}",
            reply_markup=keyboard
        )



@router.message(Command('remove'))
async def cmd_remove(message: types.Message):
    args = message.text.strip().split()
    if len(args) != 2 or not args[1].isdigit():
        await message.answer("❌ Использование: /remove <id>")
        return

    alert_id = int(args[1])
    success = await remove_alert(chat_id=message.from_user.id, alert_id=alert_id)
    if success:
        await message.answer(f"✅ Оповещение с ID {alert_id} удалено.")
    else:
        await message.answer(f"⚠️ Оповещение с ID {alert_id} не найдено.")



@router.callback_query(lambda c: c.data.startswith("delete_alert:"))
async def process_delete_callback(callback: CallbackQuery):
    try:
        alert_id = int(callback.data.split(":")[1])
        success = await remove_alert(callback.from_user.id, alert_id)
        if success:
            await callback.message.edit_text('Алерт удален')
        else:
            await callback.answer('Ошибка', show_alert=True)
    except Exception as e:
        await callback.answer(f"Ошибка: {e}", show_alert=True)