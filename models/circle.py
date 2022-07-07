from models.Figures import Figures

class Circle(Figures):
    def __init__(self, name:str, x_coordinate_of_the_center:int, y_coordinate_of_the_center:int, radius:float ):
        super().__init__(name)
        self.x_coordinate_of_the_center = x_coordinate_of_the_center
        self.y_coordinate_of_the_center = y_coordinate_of_the_center
        self.radius = radius
    def __str__(self) -> str:
        return super().__str__() + f"Center A({self.x_coordinate_of_the_center};" \
                                   f"{self.y_coordinate_of_the_center}), radius = {self.radius}"
    def feature(self) -> str:
        feature = "I circle and I am very evenly drawn\n--------------"
        return feature