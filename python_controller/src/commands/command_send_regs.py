from .command import Command
from ..constants.constants import CODE_SEND_REGS
from ..utils.strings import bytes_to_hex_str
from typing import List
from time import sleep
"""
There are 32 registers of 32 bits each.
after sending the command we need to read 32x4 bytes
and print them in the console

the bank of registers should be printed with the following format:
register 0: 0x00000000
register 1: 0x00000000
...
register 31: 0x00000000

"""

class CommandSendRegs(Command):
    def __init__(self, ser, log_path):
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executing")
        self.send_code()
        sleep(0.1)
        self.ser.reset_input_buffer()
        reg_bytes = self.read_regs()
        self.print_regs(reg_bytes)

    def send_code(self):
        self.ser.write(CODE_SEND_REGS.to_bytes(1, 'big'))
    
    def read_regs(self) -> List[bytes]:
        regs = self.ser.read(32 * 4)
        return regs
    
    def print_regs(self, reg_bytes: List[bytes]):
        for i in range(0, len(reg_bytes), 4):
            reg_hex_str = bytes_to_hex_str(reg_bytes[i:i+4])
            print(f"register {i // 4}: {reg_hex_str}")
        pass