import unittest

from animals.animal_settings import FISH_SIMPLE_ENERGY
from animals.fish_simple import FishSimple


class FishTestCase(unittest.TestCase):

    def setUp(self):
        self.fish = FishSimple("Fish")

    def test_start_fish_energy_level(self):
        energy_level = self.fish.get_energy()
        self.assertEqual(energy_level, FISH_SIMPLE_ENERGY)

    def test_fish_run(self):
        energy_level = self.fish.get_energy()
        running_times = 30  # Any big enough number
        for _ in range(running_times):
            self.fish.run()
        energy_level_after_run = self.fish.get_energy()
        self.assertEqual(energy_level, energy_level_after_run)

    def test_fish_swim(self):
        energy_level = self.fish.get_energy()
        wasted_energy = self.fish.swim_behavior.wasted_energy
        energy_level -= wasted_energy
        self.fish.swim()
        energy_level_after_swim = self.fish.get_energy()
        self.assertEqual(energy_level, energy_level_after_swim)

    def test_fish_tired_after_swim(self):
        swimming_times = 30  # Any big enough number
        for _ in range(swimming_times):
            self.fish.swim()
        energy_level = self.fish.get_energy()
        self.assertGreaterEqual(energy_level, 0)

    def test_fish_fly(self):
        energy_level = self.fish.get_energy()
        flying_times = 30  # Any big enough number
        for _ in range(flying_times):
            self.fish.fly()
        energy_level_after_fly = self.fish.get_energy()
        self.assertEqual(energy_level, energy_level_after_fly)

    def test_two_fishs_swimming(self):
        start_energy_2nd_fish = 40
        fish_2 = FishSimple("Fish 2", start_energy_2nd_fish)
        energy_level_1st_fish = self.fish.get_energy()
        energy_level_2nd_fish = fish_2.get_energy()
        wasted_energy = self.fish.swim_behavior.wasted_energy
        energy_level_1st_fish -= wasted_energy
        energy_level_2nd_fish -= wasted_energy
        self.fish.swim()
        fish_2.swim()
        energy_level_after_run_1st_fish = self.fish.get_energy()
        energy_level_after_run_2nd_fish = fish_2.get_energy()
        self.assertEqual(
            energy_level_after_run_1st_fish,
            energy_level_1st_fish,
        )
        self.assertEqual(
            energy_level_after_run_2nd_fish,
            energy_level_2nd_fish,
        )
