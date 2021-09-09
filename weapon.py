import random

class Weapon:
    def __init__(self):
        self.weapon_name = ''
        self.weapon_attack_power = 0
        self.weapon_name_randomized()
        self.attack_power()

    def weapon_name_randomized (self):
        weapon_names = ["axe", "sword", "polearm", "naginata", "Throwing star", "Spear", "Dagger", "Mace"]
        self.weapon_name = random.choice(weapon_names)
        print(f'Weapon: {self.weapon_name}')
    
    def attack_power (self):
        self.weapon_attack_power = random.choice(range(25, 35))
        print(f'Weapon attack power: {self.weapon_attack_power}')