from abc import ABC, abstractmethod


class Tyre(ABC):
    def __init__(self, wear_level):
        self.wear_level = wear_level

    @abstractmethod
    def needs_service(self):
        pass
