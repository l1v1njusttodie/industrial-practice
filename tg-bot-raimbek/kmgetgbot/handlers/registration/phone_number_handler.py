from django.db.models import query
from telegram.ext import MessageHandler, filters

from kmgetgbot.utils.wrappers import wait_message
from kmgetgbot.utils.services import register_chat_id, check_phone_number_in_db
from kmgetgbot.handlers.menu.menu import menu_handler


@wait_message
async def handle_button_press(update, context):
    contact = update.message.contact.phone_number
    if contact is not None:
        chat_id = update.effective_chat.id
        is_phone_number_exist = await check_phone_number_in_db(contact)
        if is_phone_number_exist:
            await register_chat_id(chat_id, contact)
            await menu_handler(update, context)
        else:
            await context.bot.send_message(chat_id=chat_id, text="There is no information "
                                                                 "about you in the database,"
                                                                 "please type /register "
                                                                 "command to start registration")
    else:
        query.answer("Please share your contact information to proceed.")


phone_number_handler = MessageHandler(filters.CONTACT, handle_button_press)
