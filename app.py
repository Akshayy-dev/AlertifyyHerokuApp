from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler
import os

TOKEN = os.environ.get("TELEGRAM_ID")


def start(update, context):
    username = update.message.chat.first_name
    msg = "Hi " + username + "! Please follow the instructions on the Alertifyy app to add Alertifyy Bot in your group or channel.\n\nInstall the from: http://google.com/"
    # if Filters.chat_type == Filters.private:
    context.bot.sendMessage(update.message.chat_id, msg)


def getchatid(update, context):
    print(update.message.chat_id)
    # if update.message.cha != "private":

    context.bot.sendMessage(update.effective_message.chat_id, update.effective_message.chat_id)
    #context.bot.sendMessage(update.effective_chat, update.effective_chat)


def error(update, context):
    msg = "Oops! Error encountered."
    context.bot.sendMessage(update.message.chat_id, msg)


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start, filters=Filters.private))
    dp.add_handler(CommandHandler("getchatid", getchatid))  # ,filters=Filters.group))
    dp.add_handler(MessageHandler(Filters.text, getchatid))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=os.environ.get("PORT", 443),
                          url_path=TOKEN, webhook_url="https://alertifyy-telegram-bot.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
