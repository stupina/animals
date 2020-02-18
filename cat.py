from animals.abstract_animal import AbstractAnimal


class Cat(AbstractAnimal):

    def run(self):
        print("My name is "+str(self.name)+" and i running")
        self.energy = self.energy - 5

    def swim(self):
        print("My name is "+str(self.name)+" and i can't swim")

    def fly(self):
        print('My name is '+str(self.name)+" and i can't fly")
