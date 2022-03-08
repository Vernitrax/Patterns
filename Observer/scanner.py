from abc import ABC, abstractmethod
from numpy.random import choice


class Scanner(ABC):
    message = "unknown threat detected!"

    @abstractmethod
    def scan_fleet(self, ships_count: int) -> list:
        pass


class BioScanner(Scanner):
    message = "evil robots detected!"

    def scan_fleet(self, ships_count: int) -> list:
        result = []
        for i in range(ships_count):
            result.append(choice([True, False], p=[0.01, 0.99]))
        return result


class EnergyScanner(Scanner):
    message = "high energy signature, pirates detected!"

    def scan_fleet(self, ships_count: int) -> list:
        result = []
        for i in range(ships_count):
            result.append(choice([True, False], p=[0.02, 0.98]))
        return result
