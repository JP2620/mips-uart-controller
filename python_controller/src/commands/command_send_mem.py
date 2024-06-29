from .command import Command
from ..constants.constants import CODE_SEND_MEM
from ..utils.strings import bytes_to_hex_str
from typing import List

class CommandSendMem(Command):
    def __init__(self, ser, log_path):
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executed")
        self.send_code()
        mem_bytes = self.read_mem()
        self.print_mem(mem_bytes)

    def send_code(self):
        self.ser.write(CODE_SEND_MEM.to_bytes(1, 'big'))
    
    def read_mem(self) -> List[bytes]:
        mem_size = 4 * 4
        return self.ser.read(mem_size)
    
    def print_mem(self, mem_bytes: List[bytes]):
        for i in range(0, len(mem_bytes), 4):
            mem_hex_str = bytes_to_hex_str(mem_bytes[i:i+4])
            print(f"memory {i // 4}: {mem_hex_str}")

