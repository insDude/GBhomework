from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, parameters):
        self.parameters = parameters

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.parameters / 6.5) + 0.5

class Suit(Clothes):
    @property
    def consumption(self):
        return (2 * self.parameters + 0.3) / 100

coat = Coat(48)
suit = Suit(220)
print(suit + coat)
