import random

class Dinosaur:
    def __init__(self) -> None:
        self.dinosaur_name = ''
        self.dinsoaur_attack_power = 0
        self.dinosaur_health = 0
        self.energy = 0
        self.dinosaur_name_selection()
        self.dinosaur_health_generator()
        self.dinsoaur_attack_power_generator()        
        self.dinosaur_energy_generator()

    def dinosaur_name_selection (self):
        names = ["Big T", "Shredder", "Long Boi", "Ihaswings", "Tri-top", "Cloaked", "Spitter"]
        self.dinosaur_name = random.choice(names)
        print(f'Dinosaur name: {self.dinosaur_name}')

    def dinsoaur_attack_power_generator (self):
        self.dinsoaur_attack_power = random.randrange(25, 35, 5)
        print(f"{self.dinosaur_name} the dinosaur's attack Power: {self.dinsoaur_attack_power}")

    def dinosaur_health_generator (self):
        self.dinosaur_health = random.randrange(200, 250, 10)
        print(f"{self.dinosaur_name} the dinosaur's health: {self.dinosaur_health}")

    def dinosaur_energy_generator (self):
        self.energy = random.randrange(100, 130, 10)
        print(f"{self.dinosaur_name} dinosaur's energy level: {self.energy}")

    def attack (self, robot):
        pass