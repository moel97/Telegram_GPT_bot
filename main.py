from telegram.ext import *
from telegram import Update
from typing import Final
from ChatGPT_Interaction import *
from ofline_QuestionHandling import *
Token : Final = "6032445798:AAGlnHFiPKCIkdgZFJh1RGjgijG8veq7_Hc"
Bot_Username: Final = "@askmrchatgptbot"

#commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! How can I assist you today?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Of course! I'm here to help. Please let me know what you need assistance with, and I'll do my best to provide you with the information or guidance you're looking for.")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")

async def handel_message (update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f' User {update.message.chat.id}  in {message_type} : "{text}" ')

    try:
        if message_type == 'group':
            if Bot_Username in text:
                new_text: str = text.replace(Bot_Username,"")
                response: str = get_GPTanswer(new_text)
            else:
                return
        else:
             response: str = get_GPTanswer(text)
    except:
        response: str = process_question(text)

    print(f'Bot : {response}')
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f' Update {update} caused an Error {context.error}')

if __name__ == '__main__':
    print("bot started")
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handel_message))

    app.add_error_handler(error)

    print('polling')
    app.run_polling(poll_interval= 3)


