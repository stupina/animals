from animals.fly_behavior.fly_behavior import FlyBehavior


class CanNotFlyMethod(FlyBehavior):
    def perform_fly(self, animal):
        print("My name is {} and i can't fly".format(animal.name))
