from tyre.tyre import Tyre


class OctoprimeTyre(Tyre):
    def __init__(self, wear_level):
        super().__init__(wear_level)

    def needs_service(self):
        return sum(self.wear_level) >= 3
