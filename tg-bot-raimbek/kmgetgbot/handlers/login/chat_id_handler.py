from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import CallbackContext, CommandHandler

from kmgetgbot.utils.api import api
from kmgetgbot.utils.wrappers import wait_message
from kmgetgbot.handlers.menu.menu import menu_handler


@wait_message
async def handle_chat_id(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    if api.get_employee_by_chat_id(chat_id)['chat_id'] == chat_id:
        await menu_handler(update, context)

    else:
        keyboard = [[KeyboardButton(text="Share contact", request_contact=True)]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await context.bot.send_message(chat_id=chat_id, text="Share Contact", reply_markup=reply_markup)


start_handler = CommandHandler('start', handle_chat_id)



