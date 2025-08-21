from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🪨 Камень", "✂️ Ножницы", "📄 Бумага"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Давай сыграем! Выбирай:", reply_markup=reply_markup)

# Логика игры
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text
    options = ["🪨 Камень", "✂️ Ножницы", "📄 Бумага"]
    bot_choice = random.choice(options)

    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == "🪨 Камень" and bot_choice == "✂️ Ножницы") or \
         (user_choice == "✂️ Ножницы" and bot_choice == "📄 Бумага") or \
         (user_choice == "📄 Бумага" and bot_choice == "🪨 Камень"):
        result = "Ты выиграл! 🔥"
    else:
        result = "Я выиграл 😎"

    await update.message.reply_text(f"Ты выбрал: {user_choice}\nЯ выбрал: {bot_choice}\n\n{result}")

# Запуск бота
app = ApplicationBuilder().token("8366582630:AAEuV0NS6blSRJ-jfwar1ak4-gFnt_MidM4").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, play))

print("Бот запущен и ждёт команды...")

app.run_polling()
app.run_polling()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8366582630:AAEuV0NS6blSRJ-jfwar1ak4-gFnt_MidM4"

# /start команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я теперь могу работать и в группе 😎")

# Эхо-ответ (бот будет повторять любое сообщение)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(8366582630:AAEuV0NS6blSRJ-jfwar1ak4-gFnt_MidM4).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Бот запущен и ждёт сообщений...")
    app.run_polling()

if __name__ == "__main__":
    main()