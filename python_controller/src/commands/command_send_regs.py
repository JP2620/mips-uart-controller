from .command import Command

"""
There are 32 registers of 32 bits each.
after sending the command we need to read 32x4 bytes
and print them in the console
"""
class CommandSendRegs(Command):
    def __init__(self, ser, log_path):
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executed")
        
