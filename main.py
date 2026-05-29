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

# Read sensitive values from environment for deployment
TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN environment variable not set")

STICKER_ID = os.environ.get(
    "STICKER_ID",
    "CAACAgIAAxkBAAPJagTG0C9kW8QOFfHfsM1c5bFuOCsAAtijAAPtIUgYVJ5-tM3vqTsE"
)

# Flask app (Render expects the web process to bind $PORT)
web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "Bot ishlayapti!"


# Sticker handler
async def send_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    member = await context.bot.get_chat_member(chat_id, user_id)
    if member.status in ["administrator", "creator"]:
        return
    await update.message.reply_sticker(sticker=STICKER_ID)


# Build bot application
bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_sticker))


def start_bot_polling():
    print("Starting bot polling thread...")
    bot_app.run_polling()


if __name__ == "__main__":
    # Start bot in a background thread, keep Flask as the main process for Render
    t = Thread(target=start_bot_polling)
    t.start()

    port = int(os.environ.get("PORT", 10000))
    print("Web server starting on port", port)
    web_app.run(host="0.0.0.0", port=port)