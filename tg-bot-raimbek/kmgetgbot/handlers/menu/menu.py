from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import CallbackContext, MessageHandler, filters


async def menu_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    menu_buttons = [
        [KeyboardButton("Инфо")],
        [KeyboardButton("Клубы")],
        [KeyboardButton("FAQ")],
        [KeyboardButton("Новости")],
        [KeyboardButton("Программа лояльности")],
    ]
    menu_keyboard = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)
    menu_text = "Главное меню:"
    await context.bot.send_message(chat_id=chat_id, text=menu_text, reply_markup=menu_keyboard)


menu_handle = MessageHandler(filters.Regex('^<<==.*$'), menu_handler)
