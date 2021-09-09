from dinosaur import Dinosaur

class Herd:
    def __init__(self) -> None:
        self.dinosaurs = []
        self.create_herd()


    def create_herd (self):
        for i in range(3):
            self.dinosaurs.append(Dinosaur())