from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def move(self):
        pass


class EngineImpulse(Engine):
    def move(self):
        print("Impulse engine on, moving forward...")


class EngineWarp(Engine):
    def move(self):
        print("Warp engine on, warping space around the ship...")


class EngineJump(Engine):
    def move(self):
        print("Teleportation device active, jump in 3...")
