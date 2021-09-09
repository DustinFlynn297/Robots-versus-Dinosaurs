from dinosaur import Dinosaur

class Herd:
    def __init__(self) -> None:
        self.dinosaurs = [Dinosaur(), Dinosaur(), Dinosaur()]


    # create_herd (self):
    #     dinosaurs_in_fleet = int(input("How many dinosaurs would you like in the herd? "))
    #     for i in range(dinosaurs_in_fleet):
    #         self.dinosaurs.append(Dinosaur())