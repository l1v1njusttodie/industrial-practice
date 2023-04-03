import re

from telegram import Update
from telegram.ext import MessageHandler, filters, CallbackContext

from kmgetgbot.utils.api import api
from kmgetgbot.utils.chatidcheck import check_chat_id
from kmgetgbot.utils.wrappers import wait_message


@wait_message
async def get_address_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    is_chat_id_exist = await check_chat_id(chat_id)

    if is_chat_id_exist:
        last_message = {}
        text = update.message.text
        last_message[chat_id] = text
        chosen_address = re.search('(?<=Адрес: )[^.]+', text).group(0)
        if chosen_address == 'Астана':
            address_id = 1
        if chosen_address == 'Актау':
            address_id = 2
        if chosen_address == 'Атырау':
            address_id = 3
    await context.bot.send_message(chat_id=chat_id, text=api.get_address(address_id)['address'], parse_mode='html', disable_web_page_preview=False)


address_handler = MessageHandler(filters.Regex('^Адрес:.*$'), get_address_handler)
