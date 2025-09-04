import os
from telegram import Update, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

WEBAPP_URL = "https://telegram-discount.vercel.app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = InlineKeyboardButton(
        text="📲 Открыть приложение",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    keyboard = InlineKeyboardMarkup([[button]])

    await update.message.reply_text(
        "👋 Добро пожаловать в бота для хранения дисконтных карт!\n\n"
        "📥 Здесь вы можете удобно сохранять и просматривать свои дисконтные карты прямо в Telegram.\n\n"
        "Нажмите кнопку ниже, чтобы открыть приложение 👇",
        reply_markup=keyboard
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Инструкция:\n\n"
        "1. Нажмите кнопку 'Открыть приложение'\n"
        "2. Добавьте свои дисконтные карты\n"
        "3. Получайте к ним быстрый доступ в любой момент\n\n"
        "/start — запустить бота и открыть WebApp\n"
        "/help — показать эту помощь"
    )

def main():
    TOKEN = os.getenv("BOT_TOKEN")  # Читаем токен из переменной окружения
    if not TOKEN:
        raise ValueError("❌ BOT_TOKEN не задан!")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("✅ Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
