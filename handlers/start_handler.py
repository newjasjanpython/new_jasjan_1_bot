from loader import dp, db, cur
from aiogram.filters import Command
from aiogram import types

@dp.message(Command('start'))
async def welcome(msg: types.Message):
    with db:
        cur.execute("INSERT OR REPLACE INTO users (tg_id, username) VALUES (?, ?)", (
            msg.from_user.id, msg.from_user.username
        ))
    await msg.answer("""<b>Welcome to bot!</b>
Send me a youtube.com or youtu.be link to download video from YouTube""")
