# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = 'YOUR API TOKEN HERE'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
It's time to Smoke!!! \n
You can type \n
/go for Out of office \n
or 
/down for B1 fl.\n
""")

@bot.message_handler(commands=['go'])
def send_welcome(message):
    bot.reply_to(message, """\
Let's go for smoking to Out there\
""")


@bot.message_handler(commands=['down'])
def send_welcome(message):
    bot.reply_to(message, """\
Let's go for smoking to B1 place!! \
""")

@bot.message_handler(commands=['stop'])
def send_welcome(message):
    bot.reply_to(message, """\
Go back office!!!\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
