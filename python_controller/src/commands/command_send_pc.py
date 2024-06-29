from .command import Command
from ..constants.constants import CODE_SEND_PC
from typing import List
from ..utils.strings import bytes_to_hex_str

class CommandSendPc(Command):
    def __init__(self, ser, log_path):
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executing")
        self.send_code()
        pc = self.read_pc()
        self.print_pc(pc)

    def send_code(self):
        self.ser.write(CODE_SEND_PC.to_bytes(1, 'big'))
    
    def read_pc(self) -> List[bytes]:
        pc = self.ser.read(4)
        return pc
    
    def print_pc(self, pc: bytes):
        print(f"PC: {bytes_to_hex_str(pc)}")
        pass