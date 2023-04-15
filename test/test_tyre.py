import unittest
from datetime import datetime

from tyre.models.carrigan_tyre import CarriganTyre
from tyre.models.octoprime_tyre import OctoprimeTyre


class TestCarriganTyre(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        wear_level = [0.9, 0.5, 0.3, 1]

        tyre = CarriganTyre(wear_level)

        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        wear_level = [0.2, 0.5, 0.3, 0.1]

        tyre = CarriganTyre(wear_level)

        self.assertFalse(tyre.needs_service())


class TestOctoprimeTyre(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        wear_level = [0.9, 0.5, 0.8, 1]

        tyre = OctoprimeTyre(wear_level)

        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        wear_level = [0.2, 0.5, 0.3, 0.1]

        tyre = OctoprimeTyre(wear_level)

        self.assertFalse(tyre.needs_service())
