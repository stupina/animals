from animals.fly_behavior.fly_behavior import FlyBehavior


class FlyWastingEnergyMethod(FlyBehavior):
    def __init__(self, wasted_energy=30):
        self.wasted_energy = wasted_energy
        super().__init__()

    def perform_fly(self, animal):
        print("My name is {} and i flying".format(animal.name))
        animal.energy -= self.wasted_energy
