from aiogram import Dispatcher, Bot
import sqlite3


token = "6921968249:AAGD3RvAXNMMuQ4m6OICprMbdOXWFz7yllY"
bot = Bot(token)
dp = Dispatcher()
db = sqlite3.connect('db.sqlite3')
cur = db.cursor()
