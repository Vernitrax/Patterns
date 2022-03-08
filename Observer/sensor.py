from abc import ABC, abstractmethod
from random import randint

from Observer.sensor_interpreter import Interpreter


class Sensor(ABC):
    @abstractmethod
    def notify(self):
        pass


class WarpgateSensor(Sensor):
    def __init__(self, sensor_id: str, interpreter: Interpreter):
        self._id = sensor_id
        self._interpreter = interpreter

    def notify(self):
        ships_count = randint(1, 24)
        print(f"Warpgate sensor {self._id} detected new fleet arrival... {ships_count} ships.")
        self._interpreter.analyse(ships_count)
