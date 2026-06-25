import asyncio
from telegram.ext import Application
from config import BOT_TOKEN
from modules.telegram_bot import register_handlers

async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    register_handlers(app)

    print("🚀 CyberSec Job Bot Started")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    try:
        await asyncio.Event().wait()
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
