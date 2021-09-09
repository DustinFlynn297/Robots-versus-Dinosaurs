from weapon import Weapon


import random

class Robot:
    def __init__ (self):
        self.robot_name = ''
        self.robot_health = 0
        self.robot_power_level = 0
        self.robot_weapon = Weapon()
        self.robot_name_selection()
        self.robot_health_selection()
        self.robot_power_level_selection()

    def robot_name_selection (self):
        names = ["Paul", "Tristan", "Jocham", "Azrael", "Asmodeus", "Thor", "Jakobi"]
        self.robot_name = random.choice(names)
        print(f'Robot name: {self.robot_name}')

    def robot_health_selection (self):
        self.robot_health = random.choice(range(200,250))
        print(f"{self.robot_name}'s health: {self.robot_health}" )

    def robot_power_level_selection (self):
        self.robot_power_level = random.choice(range(100,125))
        print(f"{self.robot_name}'s power level: {self.robot_power_level}" )

mike = Robot()
steve = Robot