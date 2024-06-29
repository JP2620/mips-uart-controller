from constants.constants import CODE_SEND_MEM, CODE_SEND_REGS, CODE_SEND_PC, CODE_MODO_CONTINUO, CODE_MODO_PASO_A_PASO, CODE_CARGA_INSTR

class CommandFactory:
    def __init__(self, ser, log_path):
        self.ser = ser
        self.log_path = log_path

    def create_command(self, command_code):
        if command_code == CODE_SEND_MEM:
            return command_send_mem.CommandSendMem(self.ser, self.log_path)
        elif command_code == CODE_SEND_REGS:
            return command_send_regs.CommandSendRegs(self.ser, self.log_path)
        elif command_code == CODE_SEND_PC:
            return command_send_pc.CommandSendPc(self.ser, self.log_path)
        elif command_code == CODE_MODO_CONTINUO:
            return command_modo_continuo.CommandModoContinuo(self.ser, self.log_path)
        elif command_code == CODE_MODO_PASO_A_PASO:
            return command_modo_paso_a_paso.CommandModoPasoAPaso(self.ser, self.log_path)
        elif command_code == CODE_CARGA_INSTR:
            return command_carga_instr.CommandCargaInstr(self.ser, self.log_path)
        else:
            return None