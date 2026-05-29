# telegram-bot

Simple Telegram sticker bot built with python-telegram-bot and Flask.

## Requirements
- Python dependencies: see `requirements.txt`.

## Deploy to Render
1. Create a new **Web Service** on Render and connect your repository/branch.
2. In Render service settings, set the environment variables:
	- `TOKEN` — your Telegram bot token (required)
	- `STICKER_ID` — optional custom sticker id
3. Render will use the `Procfile` to start the app (`python main.py`). The Flask web server binds to `$PORT` and the bot runs polling in a background thread.

Do not commit real tokens. See `.env.example` for local testing.

## Local testing
```bash
pip install -r requirements.txt
export TOKEN="your_telegram_bot_token_here"
python main.py
```

## Notes
- For production you may prefer using Telegram webhooks instead of polling; ask if you want that change.
