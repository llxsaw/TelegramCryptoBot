import aiosqlite

DB_PATH = "alerts.db"


async def get_user_alerts(chat_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            'SELECT id, coin_id, target_price FROM alerts WHERE chat_id = ?',
            (chat_id,)
        )
        return await cursor.fetchall()

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            coin_id INTEGER NOT NULL,
            target_price REAL NOT NULL ) 
        ''')
        await db.commit()


async def add_alert_db(chat_id: int, coin_id: str, price: float):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO alerts (chat_id, coin_id, target_price) VALUES (?, ?, ?)",
            (chat_id, coin_id, price)
        )
        await db.commit()


async def get_all_alerts():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT chat_id, coin_id, target_price FROM alerts')
        return await cursor.fetchall()


async def remove_alert(chat_id: int, alert_id: int) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "DELETE FROM alerts WHERE id = ? AND chat_id = ?",
            (alert_id, chat_id)
        )
        await db.commit()
        return cursor.rowcount > 0