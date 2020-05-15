from .command import Command

class SimpleTextResponseCommand(Command):

    def __init__(self, command_name, response, filter):
        self.response = response
        super().__init__(command_name, filter)

    def command(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=self.response)