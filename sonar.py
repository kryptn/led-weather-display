from math import e, pi
from typing import Iterable, List

i = complex(0, 1)

full_circle = pi * 2

Radians = float


def unrounded_print_coord(coord: complex):
    return f"({coord.real:.2f}, {coord.imag:.2f})"


def print_coord(coord: complex):
    return f"({round(coord.real)}, {round(coord.imag)})"


def print_line(coords: List[complex]):
    return "[" + ", ".join(print_coord(c) for c in coords) + "]"


def rotate(z: complex, theta: Radians):
    return z * e ** (i * theta)


def distributed_points(distance: int, points: int):
    return [n * (distance / points) for n in range(points + 1)]


def point_line(distance: int, points: int):
    return [complex(0, n) for n in distributed_points(distance, points)]


def rotate_line(line: List[complex], theta: Radians):
    return [rotate(z, theta) for z in line]


def sonar(distance: int, points: int, ticks: int = 300) -> Iterable[List[complex]]:
    # returns the coordinates for the spinning line
    # line spins counter clockwise
    # does not return original line at the end

    # In[4]:
    # for l in sonar(20, 3, 12):
    #     print(print_line(l))
    #
    # [(0.00, 0.00), (0.00, 6.67), (0.00, 13.33), (0.00, 20.00)]
    # [(0.00, 0.00), (3.33, 5.77), (6.67, 11.55), (10.00, 17.32)]
    # [(0.00, 0.00), (5.77, 3.33), (11.55, 6.67), (17.32, 10.00)]
    # [(0.00, 0.00), (6.67, 0.00), (13.33, 0.00), (20.00, 0.00)]
    # [(0.00, 0.00), (5.77, -3.33), (11.55, -6.67), (17.32, -10.00)]
    # [(0.00, 0.00), (3.33, -5.77), (6.67, -11.55), (10.00, -17.32)]
    # [(0.00, 0.00), (0.00, -6.67), (0.00, -13.33), (0.00, -20.00)]
    # [(0.00, 0.00), (-3.33, -5.77), (-6.67, -11.55), (-10.00, -17.32)]
    # [(0.00, 0.00), (-5.77, -3.33), (-11.55, -6.67), (-17.32, -10.00)]
    # [(0.00, 0.00), (-6.67, -0.00), (-13.33, -0.00), (-20.00, -0.00)]
    # [(0.00, 0.00), (-5.77, 3.33), (-11.55, 6.67), (-17.32, 10.00)]
    # [(0.00, 0.00), (-3.33, 5.77), (-6.67, 11.55), (-10.00, 17.32)]

    line = point_line(distance, points)
    theta: Radians = (pi * 2) / ticks * -1

    for _ in range(ticks):
        yield line
        line = rotate_line(line, theta)


if __name__ == '__main__':
    for l in sonar(200, 10):
        print(print_line(l))
