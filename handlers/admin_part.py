from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor

import os

# async def on_startup(_):
#     print('Bot is online')

# # @dp.message_handler()
# async def echo_send(message : types.Message):
#     await message.answer(message.text)
#     # await message.reply(message.text)
#     # await bot.send_message(message.from_user.id, message.text)


# executor.start_polling(dp, skip_updates=True, on_startup=on_startup)