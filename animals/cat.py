from animals.abstract_animal import AbstractAnimal
from animals.animal_settings import CAT_ENERGY
from . fly_behavior.can_not_fly_method import(
    CanNotFlyMethod,
)
from . run_behavior.run_wasting_energy_method import(
    RunWastingEnergyMethod,
)
from . swim_behavior.can_not_swim_method import(
    CanNotSwimMethod,
)


class Cat(AbstractAnimal):
    def __init__(self, name, energy=CAT_ENERGY, **kwargs):
        super().__init__(name, energy, **kwargs)
        self.fly_behavior = CanNotFlyMethod()
        self.run_behavior = RunWastingEnergyMethod()
        self.swim_behavior = CanNotSwimMethod()
