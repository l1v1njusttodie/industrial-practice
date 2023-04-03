import re

from telegram import Update
from telegram.ext import MessageHandler, filters, CallbackContext

from kmgetgbot.utils.api import api
from kmgetgbot.utils.chatidcheck import check_chat_id
from kmgetgbot.utils.wrappers import wait_message


@wait_message
async def get_about_company_handler(update:Update, context: CallbackContext):
    chat_id = update.message.chat_id
    is_chat_id_exist = await check_chat_id(chat_id)

    if is_chat_id_exist:
        last_message = {}
        text = update.message.text
        last_message[chat_id] = text
        answer_id = re.search('(?<=❓)[^)]+', text).group(0)
    await context.bot.send_message(chat_id=chat_id, text=api.get_about_company(answer_id)['code'], parse_mode='html')

about_company_handler = MessageHandler(filters.Regex('^❓.*$'), get_about_company_handler)
