
from math import pi


def circle_area(radius: int | float) -> float:
    if radius < 0:
        raise ValueError("The radius of a circle cannot be negative!")
    if isinstance(radius, str):
        raise TypeError("The radius is a number and not a string")
    area = pi * (radius**2)
    return area
