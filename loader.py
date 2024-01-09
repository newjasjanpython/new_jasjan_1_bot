from aiogram import Dispatcher, Bot
import sqlite3


token = ""
bot = Bot(token, parse_mode='html')
dp = Dispatcher()
db = sqlite3.connect('db.sqlite3')
cur = db.cursor()
