from aiogram.utils import executor
from create_bot import dp
from handlers import client_part, for_regular_info
from data_base import sqlite_db
from notifications import client_notification

async def on_startup(_):
    print("Bot is online")
    sqlite_db.sql_start()
    client_notification.greeting()

client_part.register_handlers_client(dp)
for_regular_info.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)