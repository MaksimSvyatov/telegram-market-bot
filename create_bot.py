from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage=MemoryStorage()
TOKEN='5806158899:AAEF5GdihaO4lhBksUT7NI7D42ErlzVZ3io'
print(type(TOKEN))
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)