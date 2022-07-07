from models.Figures import Figures


class Rectangle(Figures):
    def __init__(self, name: str, the_length_of_the_first_side: int, the_length_of_the_second_side: int):
        super().__init__(name)
        self.the_length_of_the_first_side = the_length_of_the_first_side
        self.the_length_of_the_second_side = the_length_of_the_second_side

    def __str__(self) -> str:
        return super().__str__() + f"the length of the first side = {self.the_length_of_the_first_side}," \
                                   f" the length of the second side = {self.the_length_of_the_second_side}," \
                                   f" area = {self.the_length_of_the_first_side * self.the_length_of_the_second_side}"

    def feature(self) -> str:
        feature = "my opposite sides are equal\n--------------"
        return feature
