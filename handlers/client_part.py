from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client_part
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет. Я market-bot)', reply_markup=kb_client_part)
        await message.delete()
    except:
        await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')
        
# @dp.message_handler(commands=['Акции'])
async def command_shares(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Укажи тикер акции заглавными буквами', reply_markup=kb_client_part)
        # клавиатура останется на месте
        await message.delete()
    except:
        await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')

# @dp.message_handler(commands=['Облигации'])
async def command_bonds(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Укажи тикер облигации заглавными буквами', reply_markup=ReplyKeyboardRemove())
        # клавиатура после срабатывания хэндлера удалится безвозвратно
        await message.delete()
    except:
        await message.reply('Напишите боту в ЛС, напишите ему: \nhttps://t.me/Investment_FollowUp_bot')
        
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_shares, commands=['Акции'])
    dp.register_message_handler(command_bonds, commands=['Облигации'])