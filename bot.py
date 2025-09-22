import telebot
import os

# Token va Admin ID Railway Variables ichidan olinadi
TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "Assalomu alaykum! 👋\n\n"
        "Savollaringiz bo‘lsa, shu yerga yozishingiz mumkin.\n"
        "Xabarlaringiz menga yetib boradi ✅"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: True)
def forward_to_admin(message):
    # Xabar foydalanuvchidan keladi → admin (sen) ga forward qilinadi
    if ADMIN_ID != 0:
        bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

bot.infinity_polling()