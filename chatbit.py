import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

openai.api_key = "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"  # 👈 यहां अपनी OpenAI API Key डालो

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your ChatGPT bot 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    reply = response["choices"][0]["message"]["content"]
    await update.message.reply_text(reply)

app = ApplicationBuilder().token("8130041444:AAF6_7eyNxIWaanYMtamG19DNM107bIWqaU").build()  # 👈 यहां Bot Token डालो

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
