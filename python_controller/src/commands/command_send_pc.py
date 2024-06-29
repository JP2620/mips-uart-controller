from .command import Command

class CommandSendPc(Command):
    def __init__(self, ser, log_path):
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executed")
        pass