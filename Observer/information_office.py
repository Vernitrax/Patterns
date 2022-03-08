from abc import ABC, abstractmethod

from Observer.scanner import Scanner


class InformationOffice(ABC):
    @abstractmethod
    def report(self, ships_count: int, scanner: Scanner):
        pass


class PropagandaOffice(InformationOffice):
    def report(self, ships_count: int, scanner: Scanner):
        print(f"Military report: {ships_count} ships, " + scanner.message)
