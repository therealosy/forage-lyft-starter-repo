from engine.models.capulet_engine import CapuletEngine
from engine.models.sternman_engine import SternmanEngine
from engine.models.willoughby_engine import WilloughbyEngine

from battery.models.nubbin_battery import NubbinBattery
from battery.models.spindler_battery import SpindlerBattery

from car.car import Car


class CarFactory:
    def create_calliope(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
        )

    def create_glissade(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
        )

    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        return Car(
            SternmanEngine(warning_light_is_on),
            SpindlerBattery(last_service_date, current_date),
        )

    def create_rorschach(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
        )

    def create_thovex(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
        )
