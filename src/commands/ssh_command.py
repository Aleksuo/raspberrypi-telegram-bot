from requests import get
from .command import Command

class SSHCommand(Command):

    def __init__(self, port, ip_api, filter):
        self.port = port
        self.ip_api = ip_api
        super().__init__("ssh", filter)

    def command(self, update, context):
        ip = get('https://api.ipify.org').text
        response = "ssh pi@"+ip+" -p "+ self.port
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)