import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8896358661:AAEheeGpUrb87hU2H9_pu6oPRsGnTNuf0iK"

LIKE_API_URL = "http://127.0.0.1:5000/like?uid="

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 **স্বাগতম Free Fire Like Bot এ!**\n\n"
        "🔥 লাইক পাঠাতে: `/like <UID>`\n"
        "উদাহরণ: `/like 1234567890`"
    )

async def send_like(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ UID দিন!\nউদাহরণ: `/like 1234567890`")
        return

    uid = context.args[0]
    if not uid.isdigit():
        await update.message.reply_text("❌ সঠিক UID দিন!")
        return

    await update.message.reply_text(f"⏳ {uid} এ লাইক পাঠানো হচ্ছে...")

    try:
        response = requests.get(f"{LIKE_API_URL}{uid}", timeout=20)
        data = response.json()
        if data.get("success") or "liked" in str(data).lower():
            await update.message.reply_text(f"✅ লাইক পাঠানো হয়েছে! UID: {uid}")
        else:
            await update.message.reply_text("❌ লাইক পাঠাতে সমস্যা।")
    except:
        await update.message.reply_text("❌ এরর! API এখনো সেটআপ করা হয়নি।")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("like", send_like))
    app.run_polling()

if __name__ == "__main__":
    main()
