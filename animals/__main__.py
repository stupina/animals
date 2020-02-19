from animals.dog import Dog
from animals.tiger import Tiger


def check_animal(name, animal_cls, **kwargs):
    animal = animal_cls(name)
    animal.say()
    animal_energy = animal.get_energy()

    if "default_energy" in kwargs.keys():
        default_energy = kwargs.get("default_energy")
        err_msg = "Bad start energy for {}".format(name)
        assert animal_energy == default_energy, err_msg

    if "energy_after_run" in kwargs.keys():
        animal.run()
        energy_after_run = animal.get_energy()
        default_energy_after_run = kwargs.get("energy_after_run")
        err_msg = "Bad after run energy for {}".format(name)
        assert energy_after_run == default_energy_after_run, err_msg

    if "energy_after_swim" in kwargs.keys():
        animal.swim()
        energy_after_swim = animal.get_energy()
        default_energy_after_swim = kwargs.get("energy_after_swim")
        err_msg = "Bad after swim energy for {}".format(name)
        assert energy_after_swim == default_energy_after_swim, err_msg

    if "energy_after_fly" in kwargs.keys():
        animal.fly()
        energy_after_fly = animal.get_energy()
        default_energy_after_fly = kwargs.get("energy_after_swim")
        err_msg = "Bad after fly energy for {}".format(name)
        assert energy_after_fly == default_energy_after_fly, err_msg


def run():
    dog_args = {
        "name": "Bobik",
        "animal_cls": Dog,
        "default_energy": 100,
        "energy_after_run": 90,
        "energy_after_swim": 60,
        "energy_after_fly": 60,
    }
    check_animal(**dog_args)

    tiger_args = {
        "name": "Barsik",
        "animal_cls": Tiger,
        "default_energy": 200,
        "energy_after_run": 180,
        "energy_after_swim": 140,
        "energy_after_fly": 140,
    }
    check_animal(**tiger_args)


run()
