from animals.swim_behavior.swim_behavior import SwimBehavior


class SwimWastingEnergyMethod(SwimBehavior):
    def __init__(self, wasted_energy=30):
        self.wasted_energy = wasted_energy
        super().__init__()

    def perform_swim(self, animal):
        print("My name is {} and i swimming".format(animal.name))
        animal.energy -= self.wasted_energy
