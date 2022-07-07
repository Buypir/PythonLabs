from models.Figures import Figures


class Point(Figures):
    def __init__(self, name: str, coordinate_X: int, coordinate_Y: int):
        super().__init__(name)
        self.coordinate_X = coordinate_X
        self.coordinate_Y = coordinate_Y

    def __str__(self) -> str:
        return super().__str__() + f"Coordinates({self.coordinate_X},{self.coordinate_Y})"

    def feature(self) -> str:
        feature = "small and defenseless\n--------------"
        return feature
