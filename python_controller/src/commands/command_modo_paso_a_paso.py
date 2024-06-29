from .command import Command
from ..constants.constants import CODE_MODO_PASO_A_PASO


class CommandModoPasoAPaso(Command):
    def __init__(self, ser, log_path):
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executing")
        self.send_code()
        pass

    def send_code(self):
        self.ser.write(CODE_MODO_PASO_A_PASO.to_bytes(1, 'big'))