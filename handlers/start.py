from aiogram import Router, types
from aiogram.filters import Command
from keyboards.main_menu import main_menu

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    welcome_text = (
        "👋 Добро пожаловать в CryptoBot!\n\n"
        "Выберите действие ниже ⬇️"
    )
    await message.answer(welcome_text, reply_markup=main_menu)
    