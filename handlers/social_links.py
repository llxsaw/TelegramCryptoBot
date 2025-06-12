from aiogram import Router, types
from aiogram.filters import Command
from services.coingecko import get_coin_link

router = Router()


@router.message(Command('links'))
async def cmd_links(message: types.Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Введите название монеты, например: /links bitcoin")
        return

    coin_id = args[1].lower()
    homepage, twitter, reddit, github = await get_coin_link(coin_id)
    if all([homepage, twitter, reddit, github]) is not None:
        text = (
            f"Twiiter: {twitter}"
            f"\nReddit: {reddit}"
            f"\nGithub: {github}"
            f"\nWebsite: {homepage}"
        )
        await message.answer(text)
    else:
        await message.answer("Something went wrong.")
