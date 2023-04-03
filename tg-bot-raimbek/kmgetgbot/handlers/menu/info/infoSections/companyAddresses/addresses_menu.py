from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, filters


async def addresses_menu_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    addresses_menu_buttons = [[KeyboardButton("Адрес: Астана.")], [KeyboardButton("Адрес: Актау.")],
                              [KeyboardButton("Адрес: Атырау.")], [KeyboardButton('Назад')]]
    menu_keyboard = ReplyKeyboardMarkup(addresses_menu_buttons, resize_keyboard=True)
    await context.bot.send_message(chat_id=chat_id, text='Адреса филиалов:', reply_markup=menu_keyboard)


addresses_menu = MessageHandler(filters.Regex('Адреса'), addresses_menu_handler)
