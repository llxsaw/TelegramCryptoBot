from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    welcome_text = (
        "👋 Добро пожаловать в CryptoBot!\n\n"
        "Этот бот поможет вам отслеживать цены криптовалют и получать уведомления, "
        "когда монета достигает нужной вам цены.\n\n"
        "🔧 Что умеет бот:\n"
        "📌 Установить ценовое оповещение:\n"
        "/alert <монета> <цена>\n"
        "Пример: /alert bitcoin 70000\n\n"
        "📋 Посмотреть все активные алерты:\n"
        "/alerts_all\n\n"
        "❌ Удалить алерт по ID:\n"
        "/remove <id>\n"
        "Или просто нажмите кнопку ❌ под сообщением с алертом.\n\n"
        "🔄 Бот проверяет цены каждые 30 секунд и отправляет уведомление, "
        "если монета достигла нужного значения.\n\n"
        "💡 Монеты берутся с CoinGecko (например: bitcoin, ethereum, dogecoin)\n"
    )
    await message.answer(welcome_text)
    