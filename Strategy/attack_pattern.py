from abc import ABC, abstractmethod


class AttackPattern(ABC):
    @abstractmethod
    def attack(self):
        pass


class AttackLasers(AttackPattern):
    def attack(self):
        print("Pew pew laser guns...")


class AttackTorpedoes(AttackPattern):
    def attack(self):
        print("Launching missiles...")


class AttackSocialMedia(AttackPattern):
    def attack(self):
        print("Sending twitter posts...")
