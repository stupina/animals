from animals.run_behavior.run_behavior import RunBehavior


class RunWastingEnergyMethod(RunBehavior):
    def __init__(self, wasted_energy=5):
        self.wasted_energy = wasted_energy
        super().__init__()

    def perform_run(self, animal):
        print("My name is {} and i running".format(animal.name))
        animal.energy -= self.wasted_energy
