from robot import Robot

class Fleet:
    def __init__(self) -> None:
        self.robots = []
        self.create_fleet()



    def create_fleet(self):
        for i in range(3):
            self.robots.append(Robot())