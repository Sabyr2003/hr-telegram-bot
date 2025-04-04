import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Твой Telegram bot token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ Ошибка: TELEGRAM_BOT_TOKEN не задан!")

# Функция генерации ссылки Jitsi Meet
def create_meeting_link():
    meeting_id = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=10))
    return f"https://meet.jit.si/{meeting_id}"

# Главное меню
MAIN_MENU = [["Создать конференцию"]]
KEYBOARD = ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🔹 Нажмите кнопку, чтобы создать конференцию:", reply_markup=KEYBOARD)

# Обработчик кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text == "Создать конференцию":
        link = create_meeting_link()
        await update.message.reply_text(f"🔗 Ваша конференция: {link}")

# Создаём приложение Telegram бота
app = Application.builder().token(TOKEN).build()

# Добавляем команды
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler))

# Запускаем бота
print("✅ Бот запущен и ждёт команд...")
app.run_polling()
