import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, ConversationHandler


logger = logging.getLogger(__name__)
USERNAME, FIRSTNAME, EMAIL, PHONE_NUMBER, APPROVE = range(5)


async def start_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to this bot, newbie! "
        "Let's request your registration, but you should help me,"
        "so please, create a username for yourself",
    )
    context.user_data['registration_data'] = {}
    return USERNAME


async def ask_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("Username of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(f"Thanks, {user.first_name}, now tell me your real first name ")
    context.user_data['registration_data']['username'] = update.message.text
    return FIRSTNAME


async def ask_firstname(update: Update, context:ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("Real firstname of %s: %s", user.first_name, update.message.text)
    if user.first_name == update.message.text:
        await update.message.reply_text("Oh, so you are honest to write "
                                        "your real name in your profile ;)."
                                        "Now please, tell me your e-mail")
    else:
        await update.message.reply_text("Yup, tell me your e-mail, please")
    context.user_data['registration_data']['firstname'] = update.message.text
    return EMAIL


async def ask_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("E-mail of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Thanks, now please, write down your mobile phone number!")
    context.user_data['registration_data']['email'] = update.message.text
    return PHONE_NUMBER


async def ask_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("Mobile phone number of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text("Thanks for your registration")
    context.user_data['registration_data']['phone_number'] = update.message.text
    # return APPROVE
    await approve_registration(USERNAME, FIRSTNAME, EMAIL, PHONE_NUMBER, context)


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


async def approve_registration(username, firstname, email, phone_number, context):
    registration_data = context.user_data['registration_data']
    message = f"Registration data:" \
              f"\nUsername: {username}" \
              f"\nFirst name: {firstname}" \
              f"\nEmail: {email}" \
              f"\nPhone number: {phone_number}" \
              f"\n\nDo you approve this registration?"

    await context.bot.send_message(chat_id=602701207, text=message)
    return ConversationHandler.END

registration_handler = ConversationHandler(
    entry_points=[CommandHandler("register", start_registration)],
    states={
        USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_username)],
        FIRSTNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_firstname)],
        EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_email)],
        PHONE_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_phone_number)],
        APPROVE: [MessageHandler(filters.TEXT & ~filters.COMMAND, approve_registration)]
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

