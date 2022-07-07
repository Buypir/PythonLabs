from models.Figures import Figures


class Segment(Figures):
    def __init__(self, name: str, first_x: int, first_y: int,
                 second_x: int, second_y: int):
        super().__init__(name)
        self.first_x = first_x
        self.first_y = first_y
        self.second_x = second_x
        self.second_y = second_y

    def __str__(self) -> str:
        return super().__str__() + f"A:({self.first_x},{self.first_y}), B:({self.second_x},{self.second_y})"

    def feature(self) -> str:
        feature = "consists of two interconnected points\n--------------"
        return feature
