from Observer.sensor import WarpgateSensor
from Observer.sensor_interpreter import WarpgateInterpreter
from Observer.scanner import BioScanner, EnergyScanner
from Observer.information_office import PropagandaOffice


def main():
    bio_scanner = BioScanner(message="evil robots detected!")
    energy_scanner = EnergyScanner(message="high energy signature, pirates detected!")
    interpreter = WarpgateInterpreter(bio_scanner, energy_scanner)
    sensor = WarpgateSensor("r28-4c", interpreter)
    office = PropagandaOffice()

    interpreter.add_observer(office)

    for i in range(10):
        sensor.notify()


if __name__ == "__main__":
    main()
