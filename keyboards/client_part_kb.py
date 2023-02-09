from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# --- Main Menu ----
# shares_button = KeyboardButton("Акции")
# bonds_button = KeyboardButton("Облигации")
main_menu_button = KeyboardButton("Главное меню")
additional_info_button = InlineKeyboardButton(text="Получить дополнительную информацию", callback_data="get_add_info")
# share_client_number = KeyboardButton('Поделиться номером', request_contact=True)
# share_client_location = KeyboardButton('Пделиться местоположением', request_location=True)

# main_menu_kb_client_part = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu_with_addinfo_button = InlineKeyboardMarkup(resize_keyboard=True)
main_menu_with_addinfo_button.add(additional_info_button)
# main_menu_kb_client_part.add(shares_button).add(bonds_button)  # .row(share_client_number, share_client_number)
# main_menu_kb_client_part.add(shares_button).insert(bonds_button)
# main_menu_kb_client_part.row(shares_button, bonds_button)

# --- Shares Menu ---

# current_price_share = KeyboardButton('Узнать стоимость акции')
# share_current_price_menu_kb_client_part = ReplyKeyboardMarkup(resize_keyboard=True)

# share_current_price_menu_kb_client_part.add(additional_info_button)#.add(main_menu_button)

# --- Bonds Menu ---

# current_price_share = KeyboardButton('Узнать стоимость облигации')
# bond_current_price_menu_kb_client_part = ReplyKeyboardMarkup(resize_keyboard=True)

# bond_current_price_menu_kb_client_part.add(additional_info_button).add(main_menu_button)
