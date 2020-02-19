from animals.abstract_animal import AbstractAnimal
from animals.fly_behavior.can_not_fly_method import(
    CanNotFlyMethod,
)
from . run_behavior.run_wasting_energy_method import(
    RunWastingEnergyMethod,
)
from . swim_behavior.swim_wasting_energy_method import(
    SwimWastingEnergyMethod,
)


class Tiger(AbstractAnimal):
    def __init__(self, name, energy=200, **kwargs):
        super().__init__(name, energy, **kwargs)
        self.fly_behavior = CanNotFlyMethod()
        self.run_behavior = RunWastingEnergyMethod(20)
        self.swim_behavior = SwimWastingEnergyMethod(40)
