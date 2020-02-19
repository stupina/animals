from animals.abstract_animal import AbstractAnimal
from animals.fly_behavior.can_not_fly_method import(
    CanNotFlyMethod,
)
from . run_behavior.can_not_run_method import(
    CanNotRunMethod,
)
from . swim_behavior.swim_wasting_energy_method import(
    SwimWastingEnergyMethod,
)


class FishSimple(AbstractAnimal):
    def __init__(self, name, energy=100, **kwargs):
        super().__init__(name, energy, **kwargs)
        self.fly_behavior = CanNotFlyMethod()
        self.run_behavior = CanNotRunMethod()
        self.swim_behavior = SwimWastingEnergyMethod(5)
