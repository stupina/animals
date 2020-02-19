import unittest
from animals.duck import Duck


class DuckTestCase(unittest.TestCase):

    def setUp(self):
        self.duck = Duck("Duck")

    def test_start_duck_energy_level(self):
        energy_level = self.duck.get_energy()
        self.assertEqual(energy_level, 100)

    def test_duck_run(self):
        energy_level = self.duck.get_energy()
        running_times = 30  # Any big enough number
        for _ in range(running_times):
            self.duck.run()
        energy_level_after_run = self.duck.get_energy()
        self.assertEqual(energy_level, energy_level_after_run)

    def test_duck_swim(self):
        energy_level = self.duck.get_energy()
        wasted_energy = self.duck.swim_behavior.wasted_energy
        energy_level -= wasted_energy
        self.duck.swim()
        energy_level_after_swim = self.duck.get_energy()
        self.assertEqual(energy_level, energy_level_after_swim)

    def test_duck_tired_after_swim(self):
        swimming_times = 30  # Any big enough number
        for _ in range(swimming_times):
            self.duck.swim()
        energy_level = self.duck.get_energy()
        self.assertGreaterEqual(energy_level, 0)

    def test_duck_fly(self):
        energy_level = self.duck.get_energy()
        wasted_energy = self.duck.fly_behavior.wasted_energy
        energy_level -= wasted_energy
        self.duck.fly()
        energy_level_after_fly = self.duck.get_energy()
        self.assertEqual(energy_level, energy_level_after_fly)

    def test_duck_tired_after_fly(self):
        flying_times = 30  # Any big enough number
        for _ in range(flying_times):
            self.duck.fly()
        energy_level = self.duck.get_energy()
        self.assertGreaterEqual(energy_level, 0)

    def test_two_ducks_flying(self):
        start_energy_2nd_duck = 40
        duck_2 = Duck("Duck 2", start_energy_2nd_duck)
        energy_level_1st_duck = self.duck.get_energy()
        energy_level_2nd_duck = duck_2.get_energy()
        wasted_energy = self.duck.fly_behavior.wasted_energy
        energy_level_1st_duck -= wasted_energy
        energy_level_2nd_duck -= wasted_energy
        self.duck.fly()
        duck_2.fly()
        energy_level_after_run_1st_duck = self.duck.get_energy()
        energy_level_after_run_2nd_duck = duck_2.get_energy()
        self.assertEqual(
            energy_level_after_run_1st_duck,
            energy_level_1st_duck,
        )
        self.assertEqual(
            energy_level_after_run_2nd_duck,
            energy_level_2nd_duck,
        )
