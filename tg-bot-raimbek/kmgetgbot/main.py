import logging

from telegram.ext import ApplicationBuilder


from kmgetgbot.dispetcher import append_handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6201725037:AAFMh2_lg8slH7eiBVvLyK2NdkWKTLJryXg').build()
    application = append_handlers(application)
    application.run_polling()
