from gpiozero import CPUTemperature
from .command import Command

class TemperatureCommand(Command):

    def __init__(self, filter):
        self.cpu = CPUTemperature()
        super().__init__("temp", filter)

    def command(self, update, context):
        response = "Cpu temperature: "+self.cpu.temperature+"C"
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)