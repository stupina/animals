import unittest

from animals.animal_settings import DOG_ENERGY
from animals.dog import Dog


class DogTestCase(unittest.TestCase):

    def setUp(self):
        self.dog = Dog("Dog")

    def test_start_dog_energy_level(self):
        energy_level = self.dog.get_energy()
        self.assertEqual(energy_level, DOG_ENERGY)

    def test_dog_run(self):
        energy_level = self.dog.get_energy()
        wasted_energy = self.dog.run_behavior.wasted_energy
        energy_level -= wasted_energy
        self.dog.run()
        energy_level_after_run = self.dog.get_energy()
        self.assertEqual(energy_level, energy_level_after_run)

    def test_dog_tired_after_run(self):
        running_times = 30  # Any big enough number
        for _ in range(running_times):
            self.dog.run()
        energy_level = self.dog.get_energy()
        self.assertGreaterEqual(energy_level, 0)

    def test_dog_swim(self):
        energy_level = self.dog.get_energy()
        wasted_energy = self.dog.swim_behavior.wasted_energy
        energy_level -= wasted_energy
        self.dog.swim()
        energy_level_after_swim = self.dog.get_energy()
        self.assertEqual(energy_level, energy_level_after_swim)

    def test_dog_tired_after_swim(self):
        running_times = 50  # Any big enough number
        for _ in range(running_times):
            self.dog.swim()
        energy_level = self.dog.get_energy()
        self.assertGreaterEqual(energy_level, 0)

    def test_dog_fly(self):
        energy_level = self.dog.get_energy()
        flying_times = 30  # Any big enough number
        for _ in range(flying_times):
            self.dog.fly()
        energy_level_after_fly = self.dog.get_energy()
        self.assertEqual(energy_level, energy_level_after_fly)

    def test_two_dogs_runing(self):
        start_energy_2nd_dog = 40
        dog_2 = Dog("Dog 2", start_energy_2nd_dog)
        energy_level_1st_dog = self.dog.get_energy()
        energy_level_2nd_dog = dog_2.get_energy()
        wasted_energy = self.dog.run_behavior.wasted_energy
        energy_level_1st_dog -= wasted_energy
        energy_level_2nd_dog -= wasted_energy
        self.dog.run()
        dog_2.run()
        energy_level_after_run_1st_dog = self.dog.get_energy()
        energy_level_after_run_2nd_dog = dog_2.get_energy()
        self.assertEqual(
            energy_level_after_run_1st_dog,
            energy_level_1st_dog,
        )
        self.assertEqual(
            energy_level_after_run_2nd_dog,
            energy_level_2nd_dog,
        )
