from .command import Command
from ..constants.constants import CODE_MODO_CONTINUO

class CommandModoContinuo(Command):
    def __init__(self, ser, log_path):
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executing")
        self.send_code()

    def send_code(self):
        self.ser.write(CODE_MODO_CONTINUO.to_bytes(1, 'big'))
