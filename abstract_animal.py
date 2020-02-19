from abc import ABC
from animals.fly_behavior.fly_behavior import FlyBehavior
from animals.run_behavior.run_behavior import RunBehavior
from animals.swim_behavior.swim_behavior import SwimBehavior


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

    def fly(self):
        self.fly_behavior.perform_fly(self)

    def run(self):
        self.run_behavior.perform_run(self)

    def swim(self):
        self.swim_behavior.perform_swim(self)
