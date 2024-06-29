import serial
import time
from .src.constants.constants import CODE_CARGA_INSTR, CODE_MODO_CONTINUO, CODE_MODO_PASO_A_PASO, CODE_SEND_MEM, CODE_SEND_REGS, CODE_SEND_PC
from .src.commands.command_factory import CommandFactory
from .src.commands.command import Command

# Setup your serial connection (change 'COM3' to whatever port your device is connected to)
ser = serial.Serial('/dev/pts/7', 9600, timeout=1)  # Open serial port at 9600 baud rate

opt_command_map = {
    1: CODE_CARGA_INSTR,
    2: CODE_MODO_CONTINUO,
    3: CODE_MODO_PASO_A_PASO,
    4: CODE_SEND_MEM,
    5: CODE_SEND_REGS,
    6: CODE_SEND_PC,
    7: None
}


command_factory = CommandFactory(ser, 'logs/log.txt')

menu_str = """
Ingrese uno de los siguientes comandos:
1. CARGA_INSTR
2. MODO_CONTINUO
3. MODO_PASO_A_PASO
4. SEND_MEM
5. SEND_REGS
6. SEND_PC
7. SALIR
"""



def valid_input(command_opt):
    if int(command_opt) in opt_command_map.keys():
        return True
    return False


print(CODE_MODO_CONTINUO)
try:
    while True:
        # Input from user
        command_input = input(menu_str)

        # Check if the input is a valid command
        if not valid_input(command_input):
            print("Por favor, ingrese un comando válido.")
            continue

        command_code = opt_command_map[int(command_input)]

        # If the input is SALIR, exit the program
        if command_code is None:
            break

        # Create the command object
        command = command_factory.create_command(command_code)

        try:
            command.execute()
        except ValueError:
            # print command code in 0x format
            print(f"Something went wrong. Please try again. command_code: {command_code}")
except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    ser.close()  # Always close the serial connection