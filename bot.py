import telebot
import os

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! 👋\n\n"
        "Savollaringiz bo‘lsa, shu yerga yozishingiz mumkin.\n"
        "Xabarlaringiz menga yetib boradi ✅"
    )

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    user = message.from_user
    user_info = f"👤 Yangi xabar!\nID: {user.id}\nUsername: @{user.username}\n\n✉️ Xabar:\n{message.text}"

    # Admin (senga lichkaga)
    bot.send_message(ADMIN_ID, user_info)

    # Foydalanuvchiga javob
    bot.send_message(message.chat.id, "Savolingiz qabul qilindi ✅ Javob kuting.")

bot.infinity_polling()
