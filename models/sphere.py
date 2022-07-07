from models.Figures import Figures
import math

class Sphere(Figures):
    def __init__(self, name: str, radius: str, volume: float):
        super().__init__(name)
        self.radius = radius
        self.volume = volume


    def __str__(self) -> str:
        return super().__str__() + f"radius = {self.radius}, volume = {self.volume}"
    def feature(self) -> str:
        feature = "it is a 3d figure\n--------------"
        return feature

