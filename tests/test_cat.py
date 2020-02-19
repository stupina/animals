import unittest

from animals.animal_settings import CAT_ENERGY
from animals.cat import Cat


class CatTestCase(unittest.TestCase):

    def setUp(self):
        self.cat = Cat("Cat")

    def test_start_cat_energy_level(self):
        energy_level = self.cat.get_energy()
        self.assertEqual(energy_level, CAT_ENERGY)

    def test_cat_run(self):
        energy_level = self.cat.get_energy()
        wasted_energy = self.cat.run_behavior.wasted_energy
        energy_level -= wasted_energy
        self.cat.run()
        energy_level_after_run = self.cat.get_energy()
        self.assertEqual(energy_level, energy_level_after_run)

    def test_cat_tired_after_run(self):
        running_times = 30  # Any big enough number
        for _ in range(running_times):
            self.cat.run()
        energy_level = self.cat.get_energy()
        self.assertGreaterEqual(energy_level, 0)

    def test_cat_swim(self):
        energy_level = self.cat.get_energy()
        swimming_times = 30  # Any big enough number
        for _ in range(swimming_times):
            self.cat.swim()
        energy_level_after_swim = self.cat.get_energy()
        self.assertEqual(energy_level, energy_level_after_swim)

    def test_cat_fly(self):
        energy_level = self.cat.get_energy()
        flying_times = 30  # Any big enough number
        for _ in range(flying_times):
            self.cat.fly()
        energy_level_after_fly = self.cat.get_energy()
        self.assertEqual(energy_level, energy_level_after_fly)

    def test_two_cats_runing(self):
        start_energy_2nd_cat = 40
        cat_2 = Cat("Cat 2", start_energy_2nd_cat)
        energy_level_1st_cat = self.cat.get_energy()
        energy_level_2nd_cat = cat_2.get_energy()
        wasted_energy = self.cat.run_behavior.wasted_energy
        energy_level_1st_cat -= wasted_energy
        energy_level_2nd_cat -= wasted_energy
        self.cat.run()
        cat_2.run()
        energy_level_after_run_1st_cat = self.cat.get_energy()
        energy_level_after_run_2nd_cat = cat_2.get_energy()
        self.assertEqual(
            energy_level_after_run_1st_cat,
            energy_level_1st_cat,
        )
        self.assertEqual(
            energy_level_after_run_2nd_cat,
            energy_level_2nd_cat,
        )
