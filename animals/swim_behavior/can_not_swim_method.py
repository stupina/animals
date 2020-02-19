from animals.swim_behavior.swim_behavior import SwimBehavior


class CanNotSwimMethod(SwimBehavior):
    def perform_swim(self, animal):
        print("My name is {} and i can't swim".format(animal.name))
