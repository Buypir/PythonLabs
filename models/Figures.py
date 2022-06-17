from abc import ABC, abstractmethod


class Figures(ABC):
    def __init__(self, name: str, ):
        self.name = name

    def __str__(self) -> str:
        return f"name: {self.name}, "

    @abstractmethod
    def feature(self) -> str:
        pass
