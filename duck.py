from animals.abstract_animal import AbstractAnimal


class Duck(AbstractAnimal):

    def run(self):
        print("My name is "+str(self.name)+' and i can\'t run')

    def swim(self):
        print("My name is "+str(self.name)+" and i swimming")
        self.energy = self.energy - 10

    def fly(self):
        print("My name is "+str(self.name)+" and i flying")
        self.energy = self.energy - 30
