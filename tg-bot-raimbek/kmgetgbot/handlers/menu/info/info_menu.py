from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, filters


async def info_menu_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    info_menu_buttons = [[KeyboardButton("О компании")], [KeyboardButton("Адреса")], [KeyboardButton("Руководство")],
                         [KeyboardButton("Контакты")], [KeyboardButton("Куратор")], [KeyboardButton('<<==')]]
    menu_keyboard = ReplyKeyboardMarkup(info_menu_buttons, resize_keyboard=True)
    await context.bot.send_message(chat_id=chat_id, text='Информация', reply_markup=menu_keyboard)


info_menu = MessageHandler(filters.Regex('Инфо'), info_menu_handler)
about_menu_handler = MessageHandler(filters.Regex('^Назад.*$'), info_menu_handler)
