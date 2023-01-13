from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# , ReplyKeyboardRemove

shares_button = KeyboardButton('/Акции')
bonds_button = KeyboardButton('/Облигации')
# share_client_number = KeyboardButton('Поделиться номером', request_contact=True)
# share_client_location = KeyboardButton('Пделиться местоположением', request_location=True)

kb_client_part = ReplyKeyboardMarkup(resize_keyboard=True)

# kb_client_part.add(shares_button).add(bonds_button).row(share_client_number, share_client_number)
# kb_client_part.add(shares_button).insert(bonds_button)
# kb_client_part.row(shares_button, bonds_button)
 