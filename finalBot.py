import logging
from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update, ReplyKeyboardMarkup
from utils import get_reply, fetch_news, topics_keyboard
#enable logging
logging.basicConfig(format = '%(asctime)s - %(name)s - %(message)s', level = logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "1158559291:AAGDQvAIkLh4mPB290xQV-MBtAfpyUz-Ec8"

#Flask part
app = Flask(__name__)

@app.route('/')
def index():
    return "Suck it Jian Yang"

@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    #webhook view which reveives updates from telegram
    #create update object from json-format request.data
    update = Update.de_json(request.get_json(), bot)
    #process update
    dp.process_update(update)
    return "ok"
#Flask part

def start(bot, update):
    print(update)
    author = update.message.from_user.first_name
    reply = "Hi {} I'm uh Jian Yang and my uncle in Beijing is vehry corrupt".format(author)
    bot.send_message(chat_id = update.message.chat_id, text = reply)

def _help(bot, update):
    help_txt = "If your name is Erichu Bacheman I won't help you, die pig."
    bot.send_message(chat_id = update.message.chat_id, text = help_txt)

def news(bot, update):
    #ReplyKeyboardMarkup
    bot.send_message(chat_id=update.message.chat_id, text = "Choose a category ",
    reply_markup = ReplyKeyboardMarkup(keyboard = topics_keyboard, one_time_keyboard = True))

def reply_text(bot, update):
    intent, reply = get_reply(update.message.text, update.message.chat_id)
    if intent == "get_news":
        articles = fetch_news(reply)
        for article in articles:  
            bot.send_message(chat_id = update.message.chat_id, text = article['title'])
    else:
        bot.send_message(chat_id = update.message.chat_id, text = reply)

def echo_sticker(bot, update):
    bot.send_sticker(chat_id = update.message.chat_id, sticker = update.message.sticker.file_id)

def error(bot, update):
    author = update.message.from_user.first_name
    logger.error("You just uh destroy my rehfrigerator {}.\n Update {} caused error {}".format(author, update, update.error))


bot = Bot(TOKEN)
try:
    bot.set_webhook("https://c022adfde99c.ngrok.io/" + TOKEN)
except Exception as e:
    print(e)

#Dispatcher
dp = Dispatcher(bot, None) #None is an update_queue
#The dispatcher will have multiple handlers
dp.add_handler(CommandHandler("start",start))
dp.add_handler(CommandHandler("help",_help))
dp.add_handler(CommandHandler("news", news))
dp.add_handler(MessageHandler(Filters.text,reply_text))
dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
dp.add_error_handler(error)

if __name__ == "__main__":
    app.run(port = 8443)