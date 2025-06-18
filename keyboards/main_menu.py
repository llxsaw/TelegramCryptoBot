from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📈 Курсы валют')],
        [KeyboardButton(text='🛎 Мои алерты')],
        [KeyboardButton(text='➕ Добавить алерт')],
        [KeyboardButton(text='⚙ Настройки')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие:'
)