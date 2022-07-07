from models.Point import Point
from models.circle import Circle
from models.sphere import Sphere
from models.segment import Segment
from models.rectangle import Rectangle
from models.parallelepiped import Parallelepiped


def main() -> None:
    tochka = Point("tochka", 4, 2)
    print(tochka)
    print(tochka.feature())
    liniya = Segment("liniya", 2, 7, 9, 3)
    print(liniya)
    print(liniya.feature())
    krug = Circle("krug", 0, 0, 2.5)
    print(krug)
    print(krug.feature())
    pryamokytnuk = Rectangle("pryamokytnuk", 4, 7)
    print(pryamokytnuk)
    print(pryamokytnuk.feature())
    sphere = Sphere("3-D krug", 8, 24)
    print(sphere)
    print(sphere.feature())
    paralelepiped = Parallelepiped("Paralelepiped", 124, 221.4, "pryamokytnui")
    print(paralelepiped)
    print(paralelepiped.feature())


if __name__ == "__main__":
    main()
