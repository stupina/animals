import unittest
from animals.tiger import Tiger


class TigerTestCase(unittest.TestCase):

    def setUp(self):
        self.tiger = Tiger("Tiger")

    def test_start_tiger_energy_level(self):
        energy_level = self.tiger.get_energy()
        self.assertEqual(energy_level, 200)

    def test_tiger_run(self):
        energy_level = self.tiger.get_energy()
        wasted_energy = self.tiger.run_behavior.wasted_energy
        energy_level -= wasted_energy
        self.tiger.run()
        energy_level_after_run = self.tiger.get_energy()
        self.assertEqual(energy_level, energy_level_after_run)

    def test_tiger_tired_after_run(self):
        running_times = 30  # Any big enough number
        for _ in range(running_times):
            self.tiger.run()
        energy_level = self.tiger.get_energy()
        self.assertGreaterEqual(energy_level, 0)

    def test_tiger_swim(self):
        energy_level = self.tiger.get_energy()
        wasted_energy = self.tiger.swim_behavior.wasted_energy
        energy_level -= wasted_energy
        self.tiger.swim()
        energy_level_after_swim = self.tiger.get_energy()
        self.assertEqual(energy_level, energy_level_after_swim)

    def test_tiger_tired_after_swim(self):
        running_times = 50  # Any big enough number
        for _ in range(running_times):
            self.tiger.swim()
        energy_level = self.tiger.get_energy()
        self.assertGreaterEqual(energy_level, 0)

    def test_tiger_fly(self):
        energy_level = self.tiger.get_energy()
        flying_times = 30  # Any big enough number
        for _ in range(flying_times):
            self.tiger.fly()
        energy_level_after_fly = self.tiger.get_energy()
        self.assertEqual(energy_level, energy_level_after_fly)

    def test_two_tigers_runing(self):
        start_energy_2nd_tiger = 40
        tiger_2 = Tiger("Tiger 2", start_energy_2nd_tiger)
        energy_level_1st_tiger = self.tiger.get_energy()
        energy_level_2nd_tiger = tiger_2.get_energy()
        wasted_energy = self.tiger.run_behavior.wasted_energy
        energy_level_1st_tiger -= wasted_energy
        energy_level_2nd_tiger -= wasted_energy
        self.tiger.run()
        tiger_2.run()
        energy_level_after_run_1st_tiger = self.tiger.get_energy()
        energy_level_after_run_2nd_tiger = tiger_2.get_energy()
        self.assertEqual(
            energy_level_after_run_1st_tiger,
            energy_level_1st_tiger,
        )
        self.assertEqual(
            energy_level_after_run_2nd_tiger,
            energy_level_2nd_tiger,
        )
