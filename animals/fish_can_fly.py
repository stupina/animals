from animals.abstract_animal import AbstractAnimal
from animals.fly_behavior.fly_wasting_energy_method import(
    FlyWastingEnergyMethod,
)
from . run_behavior.can_not_run_method import(
    CanNotRunMethod,
)
from . swim_behavior.swim_wasting_energy_method import(
    SwimWastingEnergyMethod,
)


class FishCanFly(AbstractAnimal):
    def __init__(self, name, energy=100, **kwargs):
        super().__init__(name, energy, **kwargs)
        self.fly_behavior = FlyWastingEnergyMethod(20)
        self.run_behavior = CanNotRunMethod()
        self.swim_behavior = SwimWastingEnergyMethod(5)
