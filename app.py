import requests
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

    context.bot.sendMessage(update.effective_chat.id, update.effective_chat.id)

    # channel_id = update.message.forward_from_chat.id
    # print(channel_id)
    # context.bot.send_message(channel_id, text="example")

    #context.bot.sendMessage(chat_id=update.effective_chat.id, text=update.effective_chat.id)

    # api = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={channel_id}&text={"text"}'
    # response = requests.get(api).json()
    # if "/getchatid" in str(update.effective_message.text):
    #     context.bot.sendMessage(update.effective_chat, update.effective_chat)


def error(update, context):
    msg = "Oops! Error encountered."
    context.bot.sendMessage(update.effective_chat.id, update.effective_chat.id)


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start, filters=Filters.private))
    dp.add_handler(CommandHandler("getchatid", getchatid))  # ,filters=Filters.group))
    #dp.add_handler(MessageHandler(Filters.text & (~Filters.command), getchatid))

    dp.add_handler(MessageHandler(Filters.regex('^getchatid$'), getchatid))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=os.environ.get("PORT", 443),
                          url_path=TOKEN, webhook_url="https://alertifyy-telegram-bot.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()

# import os
# import telebot
#
# # print(my_secret)
# bot = telebot.TeleBot(TOKEN)
#
#
# # telebot.TeleBot
# @bot.message_handler(commands=['Greet'])
# def greet(message):
#     bot.reply_to(message, "Howdy!")
#
#
# @bot.channel_post_handler(commands=['getchatid'])
# def getchatid(message):
#     print(message.chat.id)
#     if message.chat.type != "private":
#         bot.send_message(message.chat.id, message.chat.id)
#
#
# @bot.message_handler(commands=['getchatid'])
# def getchatid(message):
#     print(message.chat.id)
#     if message.chat.type != "private":
#         # print(message.chat.id)
#         bot.reply_to(message, message.chat.id)
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     print(message.chat.id)
#     if message.chat.type == "private":
#         # print(message.chat.id)
#         bot.reply_to(message,
#                      "Please do follow the instructions on the Alertifyy app to add Alertifyy Bot in your group or channel.\n\nInstall the from: http://google.com/")
#
#
# def main():
#     bot.infinity_polling()
#
#
# if __name__ == '__main__':
#     main()
