from loader import dp, db, cur
from aiogram import types


@dp.callback_query(lambda data: str(data.data).startswith('download_'))
async def get_video_db(data: types.CallbackQuery):
    uid = data.data.replace('download_', '').strip()
    video = cur.execute("SELECT download_url FROM vids WHERE uid=?", (uid,)).fetchone()

    await data.message.answer("Yulab olish uchun tugmani bosing.", reply_markup=types.InlineKeyboardMarkup(
        inline_keyboard=[[types.InlineKeyboardButton(text="Yuklab olish", url=video[0])]]
    ))
    await data.answer()
