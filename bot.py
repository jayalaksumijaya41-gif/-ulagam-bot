
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '8241522100:AAF2aTsyf20ToZiSEKv5C38vShseItX3ICk'
bot = telebot.TeleBot(TOKEN)

CHANNEL_USERNAME = "@Kattuparur"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.from_user.id
    try:
        chat_member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if chat_member.status in ['left', 'kicked']:
            raise Exception("User not in channel")
    except Exception:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Join Channel 📢", url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"))
        markup.add(InlineKeyboardButton("♻️ Try Again", url=f"https://t.me/{bot.get_me().username}?start=start"))
        
        bot.reply_to(
            message, 
            "**Please Join Our Channel To Use Me!**", 
            reply_markup=markup, 
            parse_mode="Markdown"
        )
        return

    bot.reply_to(message, "வணக்கம்! நீங்கள் சேனலில் இணைந்துவிட்டீர்கள். பாட் இப்போது தயாராக உள்ளது!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
