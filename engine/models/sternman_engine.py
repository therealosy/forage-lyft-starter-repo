from abc import ABC

from engine.engine import Engine


class SternmanEngine(Car, ABC):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        self.warning_light_is_on
