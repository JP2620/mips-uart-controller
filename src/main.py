import serial
import time
from constants.constants import CODE_CARGA_INSTR, CODE_MODO_CONTINUO, CODE_MODO_PASO_A_PASO

# Setup your serial connection (change 'COM3' to whatever port your device is connected to)
ser = serial.Serial('/dev/pts/7', 9600, timeout=1)  # Open serial port at 9600 baud rate

menu_str = """
Ingrese uno de los siguientes comandos:
1. CARGA_INSTR
2. MODO_CONTINUO
3. MODO_PASO_A_PASO
4. Salir
"""

opt_command_map = {
    1: CODE_CARGA_INSTR,
    2: CODE_MODO_CONTINUO,
    3: CODE_MODO_PASO_A_PASO,
    4: None
}

def valid_input(command_opt):
    if int(command_opt) in [1, 2, 3, 4]:
        return True
    return False

def get_command_code(command_opt):
    return opt_command_map[int(command_opt)]


print(CODE_MODO_CONTINUO)
try:
    while True:
        # Input from user
        command_input = input(menu_str)

        # Check if the input is a valid command
        if not valid_input(command_input):
            print("Por favor, ingrese un comando válido.")
            continue

        command_code = get_command_code(command_input)

        # If the input is SALIR, exit the program
        if command_code is None:
            break

        try:
            print(f"Sending command code: {command_code}")
            # Send byte
            ser.write(command_code.to_bytes(1, byteorder='big'))
            print(f"Sent: {command_code}")
        except ValueError:
            # print command code in 0x format
            print(f"Something went wrong. Please try again. command_code: {command_code}")
except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    ser.close()  # Always close the serial connection