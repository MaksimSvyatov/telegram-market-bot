from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove



# --- Main Menu ----
shares_button = KeyboardButton("Акции")
bonds_button = KeyboardButton("Облигации")
main_menu_button = KeyboardButton("Главное меню")
additional_info_button = KeyboardButton("Получить дополнительную информацию")
# share_client_number = KeyboardButton('Поделиться номером', request_contact=True)
# share_client_location = KeyboardButton('Пделиться местоположением', request_location=True)

main_menu_kb_client_part = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu_kb_client_part.add(shares_button).add(bonds_button)  # .row(share_client_number, share_client_number)
# main_menu_kb_client_part.add(shares_button).insert(bonds_button)
# main_menu_kb_client_part.row(shares_button, bonds_button)

# --- Shares Menu ---

# current_price_share = KeyboardButton('Узнать стоимость акции')
share_current_price_menu_kb_client_part = ReplyKeyboardMarkup(resize_keyboard=True)

share_current_price_menu_kb_client_part.add(additional_info_button).add(main_menu_button)

# --- Bonds Menu ---

# current_price_share = KeyboardButton('Узнать стоимость облигации')
bond_current_price_menu_kb_client_part = ReplyKeyboardMarkup(resize_keyboard=True)

bond_current_price_menu_kb_client_part.add(additional_info_button).add(main_menu_button)
