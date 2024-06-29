from constants.constants import CODE_SEND_MEM, CODE_SEND_REGS, CODE_SEND_PC, CODE_MODO_CONTINUO, CODE_MODO_PASO_A_PASO, CODE_CARGA_INSTR
from .command_modo_continuo import CommandModoContinuo
from .command_modo_paso_a_paso import CommandModoPasoAPaso
from .command_send_mem import CommandSendMem
from .command_send_pc import CommandSendPc
from .command_send_regs import CommandSendRegs
from .command_carga_instruccones import CommandCargaInstrucciones

class CommandFactory:
    def __init__(self, ser, log_path):
        self.ser = ser
        self.log_path = log_path

    def create_command(self, command_code):
        if command_code == CODE_SEND_MEM:
            return CommandSendMem(self.ser, self.log_path)
        elif command_code == CODE_SEND_REGS:
            return CommandSendRegs(self.ser, self.log_path)
        elif command_code == CODE_SEND_PC:
            return CommandSendPc(self.ser, self.log_path)
        elif command_code == CODE_MODO_CONTINUO:
            return CommandModoContinuo(self.ser, self.log_path)
        elif command_code == CODE_MODO_PASO_A_PASO:
            return CommandModoPasoAPaso(self.ser, self.log_path)
        elif command_code == CODE_CARGA_INSTR:
            return CommandCargaInstrucciones(self.ser, self.log_path)
        else:
            return None