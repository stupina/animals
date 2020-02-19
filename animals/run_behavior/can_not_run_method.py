from animals.run_behavior.run_behavior import RunBehavior


class CanNotRunMethod(RunBehavior):
    def perform_run(self, animal):
        print("My name is {} and i can't run".format(animal.name))
