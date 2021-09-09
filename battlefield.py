from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()
        self.run_game()  

        
    def run_game(self):
        self.display_welcome()


    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs!')
     

    def battle(self):
        game_over = False
        while game_over:
            game_over = self.dino_turn()
            if game_over == True:
                return "Dinosaurs"
            game_over = self.robot_turn()
            if game_over == True:
                return "Robots"
                

    def dino_turn(self, dinosaur, robot):
        self.herd.dinosaur[dinosaur].dinosaur_attack(self.fleet.robots[robot])
        for robot in self.fleet.robots:
            if robot.alive == True:
                return True
        return False

    def robot_turn(self, robot):
        robot.robot_attack
    
    def show_dino_opponent(self):
        for i in self.fleet:
            return self.fleet[i]

    def show_robot_opponent(self):
        for i in self.herd:
            return self.herd[i]

    def display_winners(self, winner):
        if winner == "Dinosaurs":
            print("Dinosaurs have won and proceed to rule the world")
        elif winner == "Robots":
            print("Robots are the victors")