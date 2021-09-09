from robot import Robot

class Fleet:
    def __init__(self) -> None:
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robots_in_fleet = int(input("How many robots would you like in your fleet?"))
        for i in range(robots_in_fleet):
            self.robots.append(Robot())