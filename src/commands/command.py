from abc import ABC, abstractmethod

# Command Pattern
class Command(ABC):
    def __init__(self, ser, log_path):
        self.ser: serial.Serial = ser
        self.log_path = log_path
        self.log = open(log_path, "a")

    @abstractmethod
    def execute(self, log_path):
        pass

    # destructor
    def __del__(self):
        self.log.close()
