import re

from telegram import ReplyKeyboardMarkup, Update,  KeyboardButton
from telegram.ext import CallbackContext, MessageHandler, filters

from kmgetgbot.utils.chatidcheck import check_chat_id
from kmgetgbot.utils.api import api
from kmgetgbot.utils.wrappers import wait_message


@wait_message
async def faq_button_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    is_chat_id_exist = await check_chat_id(chat_id)
    if is_chat_id_exist:
        api.get_faq_list()

        buttons = []
        buttons.append([KeyboardButton('<<==')])
        for faq in api.get_faq_list():
            buttons.append([KeyboardButton('Вопрос ' + str(faq['faq_id']) + ': ' + faq['question'])])

        faq_keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
        faq_text = 'На какой вопрос вы хотите узнать ответ?:'
        await context.bot.send_message(chat_id=chat_id, text=faq_text, reply_markup=faq_keyboard)


@wait_message
async def get_answer_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    is_chat_id_exist = await check_chat_id(chat_id)

    if is_chat_id_exist:
        last_message = {}
        text = update.message.text
        last_message[chat_id] = text
        answer_id = re.search('(?<=Вопрос\s)[^:]+', text).group(0)
    await context.bot.send_message(chat_id=chat_id, text=api.get_answer_by_id(answer_id)['answer'])


faq_handler = MessageHandler(filters.Regex('FAQ'), faq_button_handler)

answer_handler = MessageHandler(filters.Regex('^Вопрос.*$'), get_answer_handler)