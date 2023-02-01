from aiogram.utils import executor
from create_bot import dp
# import keyboards.client_part_kb as nav

async def on_startup(_):
    print('Bot is online')
    
from handlers import client_part, admin_part#, other_part

client_part.register_handlers_client(dp)
admin_part.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)