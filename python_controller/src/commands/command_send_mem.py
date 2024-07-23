from .command import Command
from ..constants.constants import CODE_SEND_MEM
from ..utils.strings import bytes_to_hex_str
from typing import List
from time import sleep

class CommandSendMem(Command):
    def __init__(self, ser, log_path):
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executed")
        self.ser.reset_input_buffer()
        sleep(0.1)
        # reset the buffer
        self.send_code()
        sleep(0.1)
        #self.ser.reset_input_buffer()
        mem_bytes = self.read_mem()
        self.print_mem(self.swap_bytes(bytes_to_hex_str(mem_bytes)))


    def send_code(self):
        self.ser.write(CODE_SEND_MEM.to_bytes(1, 'big'))
    
    def read_mem(self) -> List[bytes]:
        mem_size = 256 * 4
        mem = bytearray(self.ser.read(mem_size))
        print(mem)
        sleep(0.1)
        # reset the buffer
        self.ser.reset_input_buffer()
        return list(mem)
    
    def print_mem(self, mem_bytes: List[bytes]):
        for i in range(0, len(mem_bytes), 4):
            mem_hex_str = bytes_to_hex_str(mem_bytes[i:i+4])
            print(f"memory {i // 4}: {mem_hex_str}")
    
    def swap_bytes(self, hex_string):
        # Split the string into bytes (each byte is 2 hex digits)
        bytes_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
        # Reverse the order of bytes
        bytes_list.reverse()
        # Join back into a single string
        return ''.join(bytes_list)

