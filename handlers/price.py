from aiogram import Router, types
from aiogram.filters import Command
from services.coingecko import get_price

router = Router()


@router.message(Command('price'))
async def cmd_price(message: types.Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Введите название монеты, например: /price bitcoin")
        return

    coin_id = args[1].lower()
    price, change = await get_price(coin_id)

    if price is not None:
        text = (
            f"💰 Цена {(coin_id.capitalize())}: ${price}\n"
            f"📉 Изменение за 24ч: {change}%"
        )
        await message.answer(text)
    else:
        await message.answer("❌ Не удалось получить данные. Проверьте имя монеты")
