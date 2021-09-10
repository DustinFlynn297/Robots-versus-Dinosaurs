import random

class Dinosaur:
    def __init__(self) -> None:
        self.name = ''
        self.dinsoaur_attack_power = 0
        self.health = 0
        self.energy = 0
        self.alive = True
        self.dinosaur_name_selection()
        self.dinosaur_health_generator()
        self.dinsoaur_attack_power_generator()        
        self.dinosaur_energy_generator()
        self.dinosaur_attack()

    def dinosaur_name_selection(self):
        names = ["Big T", "Shredder", "Long Boi", "Ihaswings", "Tri-top", "Cloaked", "Spitter"]
        self.name = random.choice(names)
        
        # print(f'Dinosaur name: {self.dinosaur_name}')

    def dinsoaur_attack_power_generator (self):
        self.dinsoaur_attack_power = random.randrange(25, 35, 5)
        # print(f"{self.dinosaur_name} the dinosaur's attack Power: {self.dinsoaur_attack_power}")

    def dinosaur_health_generator (self):
        self.health = random.randrange(200, 250, 10)
        # print(f"{self.dinosaur_name} the dinosaur's health: {self.dinosaur_health}")

    def dinosaur_energy_generator (self):
        self.energy = random.randrange(100, 130, 10)
        # print(f"{self.dinosaur_name} dinosaur's energy level: {self.energy}")

    def dinosaur_attack (self, robot):
        robot.health -= self.dinsoaur_attack_power
        print(f"{robot.name} has {robot.health} health left")
        if robot.health <= 0:
            robot.alive = False
