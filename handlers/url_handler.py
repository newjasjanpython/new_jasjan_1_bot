from loader import dp, db, cur
from aiogram import types
import pytube
import uuid
import re

youtube_link_regex = re.compile(r'(?:https?://)?(?:www\.)?(?:youtube\.com/[^/]+/|youtu\.be/|watch\?v=)([^"&?/ ]{11})')


async def create_formats(yt: pytube.YouTube):
    board = []
    row = []
    with db:
        for stream in yt.streams:
            uid = str(uuid.uuid4())
            cur.execute("INSERT INTO vids (download_url, uid) VALUES (?, ?)",
                        (stream.url, uid))

            if len(row) == 2:
                board.append(row)
                row = []
            if stream.video_codec:
                text = f"{stream.resolution} {stream.mime_type}"
            else:
                text = f"{stream.abr} {stream.mime_type}"
            row.append(types.InlineKeyboardButton(
                text=text,
                callback_data=f'download_{uid}'
            ))
    return types.InlineKeyboardMarkup(inline_keyboard=board)


@dp.message(lambda msg: youtube_link_regex.findall(msg.text) and not msg.forward_from)
async def save_video_db(msg: types.Message):
    links = youtube_link_regex.findall(msg.text)
    
    if links:
        for link in links:
            wait_msg = await msg.answer("Wait please...")
            try:
                youtube = pytube.YouTube(f"https://www.youtube.com/watch?v={link}")
                keyboards = await create_formats(youtube)
                await msg.answer_photo(
                    youtube.thumbnail_url,
                    caption=f"Video: <b>{youtube.title}</b>\nDate: <b>{youtube.publish_date.date()}</b>",
                    reply_markup=keyboards)
            except Exception as e:
                await msg.answer(f"Error processing link {link}: {str(e)}")

            await wait_msg.delete()
