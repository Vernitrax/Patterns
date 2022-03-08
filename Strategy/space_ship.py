from Strategy.attack_pattern import *
from Strategy.engine import *

"""

Space ship 

object with following attributes:
name:str, 
_engine:Engine, strategy pattern
_attack_patterns:list[AttackPattern], 1 or more items, strategy pattern

Constructor arguments:
name:str, engine:Engine, *attack_patterns:AttackPattern

and following methods:
get_name: self-describing, returns str
set_engine: self-describing, 1 argument Engine
add_attack_pattern: adds new attack pattern to the list:attack_patterns, 1 argument AttackPattern
engage_enemy: prints messages depending on move/attack strategies

"""


class SpaceShip:

    def __init__(self, name: str, engine: Engine, *attack_patterns: AttackPattern):
        self._name = name
        self._attack_patterns = [i for i in attack_patterns]
        self._engine = engine

    def get_name(self) -> str:
        return self._name

    def add_attack_pattern(self, attack_pattern: AttackPattern):
        self._attack_patterns.append(attack_pattern)

    def set_engine(self, move_pattern: Engine):
        self._engine = move_pattern

    def engage_enemy(self):
        print(f"{self._name} engaging enemy vessel...")
        self._engine.move()
        for pattern in self._attack_patterns:
            pattern.attack()


""" Quick check """

corvette = SpaceShip("Patrol Boat 203", EngineImpulse(), AttackLasers())
cruiser = SpaceShip("Crusader 87", EngineWarp(), AttackLasers(), AttackTorpedoes())
civilian = SpaceShip("Uselessness 304", EngineImpulse(), AttackSocialMedia())

ships = [corvette, cruiser, civilian]
for ship in ships:
    ship.engage_enemy()

corvette.add_attack_pattern(AttackTorpedoes())  # adding torpedoes
corvette.set_engine(EngineJump())  # changing engine

corvette.engage_enemy()
