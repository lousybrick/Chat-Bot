import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update

logging.basicConfig(format = '%(asctime)s - %(name)s - %(message)s', level = logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "1158559291:AAGDQvAIkLh4mPB290xQV-MBtAfpyUz-Ec8"

def start(bot, update):
    print(update)
    author = update.message.from_user.first_name
    reply = "Hi {} I'm uh Jian Yang and my uncle in Beijing is vehry corrupt".format(author)
    bot.send_message(chat_id = update.message.chat_id, text = reply)

def _help(bot, update):
    help_txt = "If your name is Erichu Bacheman I won't help you, die pig."
    bot.send_message(chat_id = update.message.chat_id, text = help_txt)

def echo_text(bot, update):
    reply = update.message.text
    bot.send_message(chat_id = update.message.chat_id, text = reply)

def echo_sticker(bot, update):
    bot.send_sticker(chat_id = update.message.chat_id, sticker = update.message.sticker.file_id)

def error(bot, update):
    author = update.message.from_user.first_name
    logger.error("You just uh destroy my rehfrigerator {}.\n Update {} caused error {}".format(author, update, update.error))

if __name__ == "__main__":
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)
    
    updater.start_polling()
    logger.info("Started Polling...")
    updater.idle()