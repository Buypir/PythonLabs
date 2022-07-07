from models.Figures import Figures

class Parallelepiped(Figures):
    def __init__(self, name:str, area: float, volume: float, kind_of_parrallelepiped:str):
        super().__init__(name)
        self.area = area
        self.volume = volume
        self.kind_of_parrallelepiped = kind_of_parrallelepiped
    def __str__(self) -> str:
        return super().__str__() + f"area = {self.area}, volume = {self.volume}," \
                                   f" kind of parallelepiped = {self.kind_of_parrallelepiped}"
    def feature(self) -> str:
        feature = "consists of 6 rectangles\n--------------"
        return feature