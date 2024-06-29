from abc import ABC, abstractmethod

# Command Pattern
class Command(ABC):
    self.ser: serial.Serial = None

    def __init__(self, ser, log_path):
        self.ser = ser
        self.log_path = log_path

    @abstractmethod
    def execute(self, log_path):
        pass