from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)
import os

TOKEN = "8752747497:AAEp0ntICw2rRGT4QEmFd0zp3Tfr3KclsD0"

STICKER_ID = "CAACAgIAAxkBAAPJagTG0C9kW8QOFfHfsM1c5bFuOCsAAtijAAPtIUgYVJ5-tM3vqTsE"

# Flask
web_app = Flask('')

@web_app.route('/')
def home():
    return "Bot ishlayapti!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

# Sticker funksiyasi
async def send_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    member = await context.bot.get_chat_member(chat_id, user_id)
    if member.status in ["administrator", "creator"]:
        return
    await update.message.reply_sticker(sticker=STICKER_ID)

# Bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, send_sticker))

keep_alive()
print("Bot ishga tushdi...")
app.run_polling()