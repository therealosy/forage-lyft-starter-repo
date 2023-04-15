from tyre.tyre import Tyre


class CarriganTyre(Tyre):
    def __init__(self, wear_level):
        super().__init__(wear_level)

    def needs_service(self):
        return any(tyre_wear > 0.9 for tyre_wear in self.wear_level)
