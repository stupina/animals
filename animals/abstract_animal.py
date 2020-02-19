from abc import ABC
from enum import Enum
from functools import wraps

from animals.fly_behavior.fly_behavior import FlyBehavior
from animals.run_behavior.run_behavior import RunBehavior
from animals.swim_behavior.swim_behavior import SwimBehavior


class BehaviorType(Enum):
    fly_behavior = 1
    run_behavior = 2
    swim_behavior = 3


def check_if_animal_have_enought_energy(behavior_name):
    def middle(func):
        @wraps(func)
        def wrap(self, *args, **kwargs):
            behavior = getattr(self, behavior_name)
            if hasattr(behavior, 'wasted_energy'):
                wasted_energy = getattr(behavior, 'wasted_energy')
                energy_level = self.get_energy()
                if wasted_energy > energy_level:
                    msg = "This animal is tired! It doesn't {}".format(
                        func.__name__,
                    )
                    print(msg)
                    result = None
                else:
                    result = func(self, *args, **kwargs)
            else:
                result = func(self, *args, **kwargs)
            return result
        return wrap
    return middle


class AbstractAnimal(ABC):
    """
    Abstract class for animal creating.

    Methods:
     * say()
     * get_energy()

    Behavior methods:
     * fly()
     * run()
     * swim()

    To add behavior:
     1. Add behavior method (for example, fly())
     2. Create folder with new behavior (for examle, fly_behavior)
        and add to it abstract behavior and specific behavior types
     3. Set a abstract behavior into abstract animal
        (for example: self.fly_behavior = FlyBehavior())
        and set specific into specific animal
     4. Add new behavior to enum class BehaviorType
        to use in check_if_animal_have_enought_energy decorator
     Extra info: if behavior method waste energy set for method argument:
        self.wasted_energy - energy, which will be wasted for action
    """

    def __init__(self, name, energy=100, **kwargs):
        self.name = name
        self.energy = energy
        self.fly_behavior = FlyBehavior()
        self.run_behavior = RunBehavior()
        self.swim_behavior = SwimBehavior()
        self.__dict__.update(kwargs)
        super().__init__()

    def say(self):
        say_str = "Hello, i'm {} and my name is {}".format(
            self.__class__.__name__,
            self.name,
        )
        print(say_str)

    def get_energy(self):
        return self.energy

    @check_if_animal_have_enought_energy(BehaviorType.fly_behavior.name)
    def fly(self):
        self.fly_behavior.perform_fly(self)

    @check_if_animal_have_enought_energy(BehaviorType.run_behavior.name)
    def run(self):
        self.run_behavior.perform_run(self)

    @check_if_animal_have_enought_energy(BehaviorType.swim_behavior.name)
    def swim(self):
        self.swim_behavior.perform_swim(self)
