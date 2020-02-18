from animals.abstract_animal import AbstractAnimal


class Tiger(AbstractAnimal):
    def __init__(self, name, energy=200, **kwargs):
        super().__init__(name, energy, **kwargs)

    def run(self):
        print("My name is "+str(self.name)+" and i running")
        self.energy = self.energy - 20

    def swim(self):
        print("My name is "+str(self.name)+" and i swimming")
        self.energy = self.energy - 40

    def fly(self):
        print('My name is '+str(self.name)+" and i can't fly")
