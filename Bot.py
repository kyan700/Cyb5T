from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

TOKEN = "8594908071:AAEKIjXRBvYyAS3fBiU0UFj-zqXdC2KemJ0"
ADMINS = [7531900641]  # ضع Telegram ID

USERS = set()

def is_admin(user_id):
    return user_id in ADMINS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    USERS.add(update.effective_user.id)
    await update.message.reply_text(
        "🎓 CYSIUTT BOT\n"
        "Cybersecurity Department\n"
        "TunTec University\n\n"
        "📌 الأوامر:\n"
        "/info معلومات الدفعة\n"
        "/schedule الجداول\n"
        "/contact تواصل"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ تخصص: الأمن السيبراني\n"
        "🎓 الدفعة الخامسة\n"
        "🏫 جامعة تونتك"
    )

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 سيتم نشر الجداول هنا")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📩 تواصل مع إدارة الدفعة")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMINS:
        return

    msg = " ".join(context.args)
    for user in USERS:
        try:
            await context.bot.send_message(user, f"📢 إعلان:\n{msg}")
        except:
            pass

    await update.message.reply_text("✅ تم الإرسال")

async def files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMINS:
        return

    for user in USERS:
        try:
            await context.bot.send_document(
                chat_id=user,
                document=update.message.document.file_id
            )
        except:
            pass

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("schedule", schedule))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("broadcast", broadcast))
app.add_handler(MessageHandler(filters.Document.ALL, files))

app.run_polling()
