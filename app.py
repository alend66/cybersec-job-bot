from telegram.ext import Application
from config import BOT_TOKEN
from modules.telegram_bot import register_handlers

def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN not found. Check your .env file.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    register_handlers(app)

    print("🚀 CyberSec Job Bot Started...")

    app.run_polling()

if __name__ == "__main__":
    main()
