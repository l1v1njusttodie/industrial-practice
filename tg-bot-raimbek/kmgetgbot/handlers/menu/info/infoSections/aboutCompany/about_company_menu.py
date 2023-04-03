from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, filters


async def about_company_menu_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    about_company_menu_buttons = [[KeyboardButton("❓ 1) Описание")], [KeyboardButton("❓ 2) Задачи")],
                                  [KeyboardButton("❓ 3) Принципы")], [KeyboardButton('Назад')]]
    menu_keyboard = ReplyKeyboardMarkup(about_company_menu_buttons, resize_keyboard=True)
    await context.bot.send_message(chat_id=chat_id, text='Информация', reply_markup=menu_keyboard)


about_company_menu = MessageHandler(filters.Regex('О компании'), about_company_menu_handler)
