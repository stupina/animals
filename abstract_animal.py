from abc import ABC


class AbstractAnimal(ABC):
    def __init__(self, name, energy=100, **kwargs):
        self.name = name
        self.energy = energy
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
