from .command import Command
from typing import List

class CommandCargaInstrucciones(Command):
    def __init__(self, ser, log_path, instrucciones_path="python_controller/resources/instrucciones.mem"):
        self.instrucciones_path = instrucciones_path
        super().__init__(ser, log_path)

    def execute(self):
        print(self.__class__.__name__ + " executed")
        instrucciones = self.read_instrucciones()
        self.send_instrucciones(instrucciones)

    def read_instrucciones(self) -> List[str]:
        with open(self.instrucciones_path, 'r') as f:
            instrucciones = f.readlines()
        return instrucciones
    
    def send_instrucciones(self, instrucciones: List[str]):
        instrucciones = self.read_instrucciones()
        for instruccion in instrucciones:
            bytes_to_send = bytes.fromhex(instruccion)
            self.ser.write(bytes_to_send)
            print("sending bytes: ", bytes_to_send)
        print("instrucciones sent")
        pass
