from abc import ABC, abstractmethod


class IMove(ABC):
    @abstractmethod
    def move(self):
        pass


class IFly:
    @abstractmethod
    def fly(self):
        pass


class ISwim:
    @abstractmethod
    def swim(self):
        pass

