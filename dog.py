from animals.abstract_animal import AbstractAnimal


class Dog(AbstractAnimal):

    def run(self):
        print("My name is "+str(self.name)+" and i running")
        self.energy = self.energy - 10

    def swim(self):
        print("My name is "+str(self.name)+" and i swimming")
        self.energy = self.energy - 30

    def fly(self):
        print("My name is "+str(self.name)+" and i can't fly")
