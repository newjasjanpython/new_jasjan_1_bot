from loader import dp
from aiogram import types

@dp.message()
async def handle(msg: types.Message):
    await msg.answer("""Menga youtubedan link yuborishingiz mumkin!""")
