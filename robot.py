from weapon import Weapon


import random

class Robot:
    def __init__ (self):
        self.robot_name = ''
        self.robot_health = 0
        self.robot_power_level = 0
        self.robot_name_selection()
        self.robot_health_selection()
        self.robot_power_level_selection()
        self.robot_weapon = Weapon()
        


    def robot_name_selection (self):
        names = ["Paul", "Tristan", "Jocham", "Azrael", "Asmodeus", "Thor", "Jakobi", "Hank", "Bob", "Sarah", "Ann", "Joyce", "Kate", "Lauren"]
        self.robot_name = random.choice(names)
        # print(f'Robot name: {self.robot_name}')

    def robot_health_selection (self):
        self.robot_health = random.randrange(200, 250, 10)
        # print(f"{self.robot_name} the robot's health: {self.robot_health}" )

    def robot_power_level_selection (self):
        self.robot_power_level = random.randrange(100, 130, 10)
        # print(f"{self.robot_name} the robot's power level: {self.robot_power_level}" )

    def attack(self, dinosaur):
        dinosaur.dinosaur_health - self.weapon_attack_power