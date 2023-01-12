from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print('Bot is online')

'''***********************************КЛИЕНТСКАЯ ЧАСТЬ************************************************* '''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет. Я market-bot)')
        await message.delete()
    except:
        await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')
        
@dp.message_handler(commands=['Акции'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Укажи тикер акции заглавными буквами')
        await message.delete()
    except:
        await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')


@dp.message_handler(commands=['Облигации'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Укажи тикер облигации заглавными буквами')
        await message.delete()
    except:
        await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')

    
    
'''***********************************АДМИНСКАЯ ЧАСТЬ************************************************* '''


@dp.message_handler()
async def echo_send(message : types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)