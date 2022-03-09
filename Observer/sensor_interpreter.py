from abc import ABC, abstractmethod

from Observer.information_office import InformationOffice
from Observer.scanner import Scanner


class Observable(ABC):
    @abstractmethod
    def notify(self, ships_count: int, scanner: Scanner):
        pass

    @abstractmethod
    def add_observer(self, observer: InformationOffice):
        pass

    @abstractmethod
    def remove_observer(self, observer: InformationOffice):
        pass


class Interpreter(Observable):
    @abstractmethod
    def analyse(self, ships_count):
        pass


class WarpgateInterpreter(Interpreter):
    def __init__(self, *scanners: Scanner):
        self._scanners = [i for i in scanners]
        self._observers = []

    def analyse(self, ships_count):
        for scanner in self._scanners:
            result = scanner.scan_fleet(ships_count)
            if WarpgateInterpreter.analyse_results(result):
                print("Alarm, notifying offices...")
                self.notify(ships_count, scanner)
            else:
                print("Safe...")

    @staticmethod
    def analyse_results(result: list) -> bool:
        return True if True in result else False

    def notify(self, ships_count: int, scanner: Scanner):
        for observer in self._observers:
            observer.report(ships_count, scanner)

    def add_observer(self, observer: InformationOffice):
        self._observers.append(observer)

    def remove_observer(self, observer: InformationOffice):
        self._observers.remove(observer)
