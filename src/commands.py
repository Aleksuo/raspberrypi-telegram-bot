from requests import get

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def ssh(update,context):
    ip = get('https://api.ipify.org').text
    context.bot.send_message(chat_id=update.effective_chat.id, text="ssh pi@"+ip+":50000")

def test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BEEP!BEEP!")