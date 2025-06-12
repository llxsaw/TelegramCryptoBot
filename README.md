

````markdown
📊 Crypto Price Alert Bot

Telegram-бот для отслеживания цен криптовалют в реальном времени и создания персональных оповещений при достижении заданного порога.

🚀 Возможности

- 🔍 Получение текущей цены по любой криптовалюте (BTC, ETH, SOL и т.д.)
- 📈 Добавление оповещений: бот уведомит, когда цена достигнет заданного значения
- 📋 Просмотр всех установленных оповещений
- ❌ Удаление оповещений
- 💡 Простое управление через команды Telegram

⚙️ Используемые технологии

- [Python 3.12+](https://www.python.org/)
- [Aiogram 3.x](https://docs.aiogram.dev/)
- [CoinGecko API](https://www.coingecko.com/)
- [SQLite](https://sqlite.org/) для хранения данных


🛠 Установка и запуск

1. Клонируй репозиторий:
```` bash
   git clone https://github.com/llxsaw/TelegramCryptoBot.git
   cd crypto-alert-bot
````


2. Создай и активируй виртуальное окружение:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # или .venv\Scripts\activate на Windows
   ```

3. Установи зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создай файл `config.py` со своими API-ключами:

   ```python
   BOT_TOKEN = "your_telegram_bot_token"
   ```

5. Запусти бота:

   ```bash
   python main.py
   ```

---

## 📬 Команды бота

* `/start` — Приветственное сообщение
* `/price <symbol>` — Узнать цену (например: `/price btc`)
* `/alert <symbol> <price>` — Установить оповещение (например: `/alert eth 3000`)
* `/alerts` — Показать все оповещения
* `/remove <id>` — Удалить оповещение по ID

## 📬 Контакты/Contacts
- Telegram: @llxsaw
- Instagram: @l1xsaww
- Email: holynskyiartem.work@gmail.com