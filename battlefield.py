from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()
        self.run_game()
        self.display_welcome()
        self.battle()
        self.show_dino_opponent()
        self.show_robot_opponent()
        



    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs!')

    def battle(self):
        pass
                

    def dino_turn(self, dinosaur):
        dinosaur.dinosaur_attack

    def robot_turn(self, robot):
        robot.robot_attack
    
    def show_dino_opponent(self):
        return self.fleet[0]

    def show_robot_opponent(self):
        return self.herd[0]
