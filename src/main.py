import serial
import time

# Setup your serial connection (change 'COM3' to whatever port your device is connected to)
ser = serial.Serial('/dev/pts/6', 9600, timeout=1)  # Open serial port at 9600 baud rate

try:
    while True:
        # Input from user
        data = input("Enter a byte (0-255): ")
        try:
            # Convert string to integer
            byte_value = int(data)
            # Check if the byte value is in the correct range
            if 0 <= byte_value <= 255:
                # Send byte
                ser.write(byte_value.to_bytes(1, 'little'))
                print(f"Sent: {byte_value}")
            else:
                print("Please enter a number between 0 and 255.")
        except ValueError:
            print("Please enter a valid number.")

except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    ser.close()  # Always close the serial connection