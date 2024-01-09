from loader import dp, bot, db, cur
import asyncio
import handlers
import logging
import sys


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

with db:
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER UNIQUE,
        username TEXT
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS vids (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        download_url TEXT,
        uid TEXT
    )""")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
