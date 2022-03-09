from abc import ABC, abstractmethod
from dataclasses import dataclass

from numpy.random import choice


@dataclass
class Scanner(ABC):
    message: str

    @abstractmethod
    def scan_fleet(self, ships_count: int) -> list:
        pass


@dataclass
class BioScanner(Scanner):
    def scan_fleet(self, ships_count: int) -> list:
        result = []
        for i in range(ships_count):
            result.append(choice([True, False], p=[0.01, 0.99]))
        return result


@dataclass
class EnergyScanner(Scanner):
    def scan_fleet(self, ships_count: int) -> list:
        result = []
        for i in range(ships_count):
            result.append(choice([True, False], p=[0.02, 0.98]))
        return result
