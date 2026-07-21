import telebot

TOKEN = '8241522100:AAF2aTsyf20ToZisEKv5C38vShseItx3ICk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "வணக்கம்! நான் உங்கள் டெலிகிராம் பாட். நான் இப்போது வெற்றிகரமாக இயங்குகிறேன்!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
