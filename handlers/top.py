from aiogram import Router, types
from aiogram.filters import Command
from services.coingecko import get_top_gainers_and_losers

router = Router()


@router.message(Command('top'))
async def cmd_top(message: types.Message):
    gainers, losers = await get_top_gainers_and_losers()

    text = "🚀 <b>Топ 10 растущих</b>\n"
    for i, coin in enumerate(gainers, start=1):
        name = coin['name']
        price = round(coin['current_price'], 2)
        change = round(coin['price_change_percentage_7d_in_currency'], 2)
        text += f"{i}. {name}: {price}$ (+{change}%)\n"

    text += "\n📉 <b>Топ 10 падающих</b>\n"
    for i, coin in enumerate(losers, start=1):
        name = coin['name']
        price = round(coin['current_price'], 2)
        change = round(coin['price_change_percentage_7d_in_currency'], 2)
        text += f"{i}. {name}: {price}$ (+{change}%)\n"

    await message.answer(text, parse_mode='HTML')
