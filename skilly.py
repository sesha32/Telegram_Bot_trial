from telegram.ext import Application, CommandHandler

Token = ""

app = Application.builder().token(Token).build()

async def start(update, context):
    await update.message.reply_text("Hello! I am hiki. How can I assist you today?")
    await update.message.reply_text(
        "Available commands:\n"
        "/start -> Welcome!\n"
        "/help -> This particular message\n"
        "/content -> About\n"
        "/python -> The first topic\n"
        "/sql -> about sql\n"
        "/java -> About java\n"
        "/contact -> to contact admin"
    )

async def help(update, context):
    await update.message.reply_text(
        "Available commands:\n"
        "/start -> Welcome!\n"
        "/help -> This particular message\n"
        "/content -> About\n"
        "/python -> The first topic\n"
        "/sql -> about sql\n"
        "/java -> About java\n"
        "/contact -> to contact admin"
    )

async def content(update, context):
    await update.message.reply_text(
        "This is a bot that can help you with various topics. Use the commands to navigate through the content."
    )

async def python(update, context):
    await update.message.reply_text(
        "Python is a versatile programming language. It is widely used for web development, data analysis, artificial intelligence, and more. You can learn more about Python at https://www.python.org/"
    )

async def sql(update, context):
    await update.message.reply_text(
        "SQL (Structured Query Language) is a standard language for managing and manipulating databases. It is used to perform tasks such as querying data, updating records, and creating tables. You can learn more about SQL at https://www.w3schools.com/sql/"
    )

async def java(update, context):
    await update.message.reply_text(
        "Java is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is widely used for building enterprise-scale applications. You can learn more about Java at https://www.oracle.com/java/"
    )

async def contact(update, context):
    await update.message.reply_text(
        "You can contact the admin at:\nEmail: seshasatyasai2003@gmail.com\nTelegram: @sesha_satya_sai"
    )

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("content", content))
app.add_handler(CommandHandler("python", python))
app.add_handler(CommandHandler("sql", sql))
app.add_handler(CommandHandler("java", java))
app.add_handler(CommandHandler("contact", contact))

if __name__ == "__main__":
    app.run_polling()
