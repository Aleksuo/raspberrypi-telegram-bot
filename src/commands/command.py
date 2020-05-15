from abc import ABC, abstractmethod
from telegram.ext import CommandHandler


class Command(ABC):
    def __init__(self, command_name, filter):
        self.handler = CommandHandler(command_name, self.command, filter)

    @abstractmethod
    def command(self,update,context):
        pass

    def get_handler(self):
        return self.handler