# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import types
# from create_bot import dp, bot
# from aiogram.dispatcher import Dispatcher
# from aiogram.dispatcher.filters import Text
# import requests
# import json
# from aiogram import types, Dispatcher
# from create_bot import dp, bot
# import keyboards.client_part_kb as nav

# # ID = None

# class FSMClient(StatesGroup):
#     shares = State()
#     bonds = State()

# # @dp.message_handler(commands=['moderator'], is_chat_admin=True)
# async def start_command(message : types.Message):
#     global ID
#     ID = message.from_user.id
#     await bot.send_message(message.from_user.id, 'Выберите о чём хотели бы получить информацию!'
#                            ,        reply_markup = nav.main_menu_kb_client_part)
#     # await message.delete()

# # Начало диалога получения информации по акции
# # @dp.message_handler(commands='Загрузить', state=None)
# # async def get_share_name(message : types.Message, state=FSMClient.shares):
# #     # await FSMClient.shares.set()
# #     await message.reply('Введи тикер акции')

# # # Ловим ответ пользователя
# # # @dp.message_handler(content_types=['name'], state=FSMAdmin.name)
# async def get_share_price(message : types.Message, state : FSMClient.shares):
#     # if message.from_user.id == ID:
#         message = message.text
#         async def get_share_price(message):
#             data = requests.get(f'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{message}.json').text
#             print(data)
#             data = json.loads(data)
#             share_current_price_index = data['marketdata']['columns'].index('LCURRENTPRICE')
#             data_list = data['marketdata']['data'][0]
#             share_current_price = data_list[share_current_price_index]
#             await bot.send_message(message.from_user.id,f'Current share price is {share_current_price}')

#         await FSMClient.next()
#         # await message.reply('Загрузи фото')# если дальше есть какие-то пунткы.
#         #Этой строкой переводим бота в ожидание ответна на следующее состояние
#         # идёт по порядку class FSMAdmin(StatesGroup), ждёт следующее состояние

# # # Начало диалога по облигации
# # async def get_bond_name(message : types.Message, state=FSMClient.bonds):
# #     await FSMClient.bonds.set()
# #     await message.reply('Введи тикер облигации')

# # # @dp.message_handler(content_types=['name'], state=FSMAdmin.name)
# async def get_bond_price(message : types.Message, state : FSMClient.bonds):
#     # if message.from_user.id == ID:
#         message = message.text
#         async def get_bond_price(message):
#             if message.text[0] == 'S':
#                 data = requests.get(f'https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities/{message}.json').text
#                 data = json.loads(data)
#                 bond_current_price_index = data['marketdata']['columns'].index('LCURRENTPRICE')
#                 data_list = data['marketdata']['data'][0]
#                 bond_current_price = data_list[bond_current_price_index]
#                 await bot.send_message(message.from_user.id,f'Current bond price is {bond_current_price}')
#             else:
#                 data = requests.get(f'https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQCB/securities/{message}.json').text
#                 data = json.loads(data)
#                 bond_current_price_index = data['marketdata']['columns'].index('LCURRENTPRICE')
#                 data_list = data['marketdata']['data'][0]
#                 bond_current_price = data_list[bond_current_price_index]
#                 await bot.send_message(message.from_user.id,f'Current bond price is {bond_current_price}')

#         # await FSMClient.next()
#         # await message.reply('Загрузи фото')# если дальше есть какие-то пунткы.
#         #Этой строкой переводим бота в ожидание ответна на следующее состояние
#         # идёт по порядку class FSMAdmin(StatesGroup), ждёт следующее состояние
# # # Ловим первый ответ админа
# # # @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
# # async def load_photo(message : types.Message, state : FSMContext):
# #     if message.from_user.id == ID:
# #         async with state.proxy() as data:
# #             data['photo'] = message.photo[0].file_id
# #         await FSMAdmin.next()
#         # await message.reply('Теперь введи название')

#         # await message.reply('Теперь введи название')
#         await state.finish() # эта строка для последнего состояния, бот выходит из машины состояний и всё очищается

# # # Выход из машины состояний
# # # @dp.message_handler(state='*', commands='отмена')
# # # @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
# # async def cancel_handler(message : types.Message, state: FSMContext):
# #     current_state = await state.get_state()
# #     if current_state is None:
# #         return
# #     await state.finish()
# #     await message.reply('Ok')

# #     # Регистрация хэндлерова
# def register_handlers_admin(dp : Dispatcher):
#     dp.register_message_handler(start_command, commands=['start'])
#     # dp.register_message_handler(get_share_name, commands=['Акции'], state=FSMClient.shares)
#     dp.register_message_handler(get_share_price, state=FSMClient.shares)
#     # dp.register_message_handler(get_bond_name, commands=['Облигации'], state=FSMClient.bonds)
#     dp.register_message_handler(get_bond_price, state=FSMClient.bonds)
# #     dp.register_message_handler(load_photo, commands=['Загрузить фото'], state=None)
# #     dp.register_message_handler(cancel_handler, state='*', commands='отмена')
# #     dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
