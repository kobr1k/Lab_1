"""
7. За довжинами двох сторін деякого трикутника і кутом між ними знайти довжину третьої сторони і
площу цього трикутника.
"""


import math


def triangle(side_1: float, side_2: float, a: float):
    side_3 = math.sqrt(side_1 ** 2 + side_2 ** 2 - 0.5 * side_1 * side_2 * (math.cos(a)))
    p = (side_1 + side_2 + side_3) / 3
    square_tr = math.sqrt(p * (p - side_1) * (p - side_2) * (p - side_3))
    return f'Side_AC = {side_3}\nSquare = {square_tr}'


def main(a: float, b: float, angle_: float):
    if a > 0 and b > 0 and (angle_ > 0 or angle_ < 180):
        triangle(a, b, angle_)
    else:
        return 'Error'


if __name__ == '__main__':
    side_a = float(input('Enter side AB:'))
    side_b = float(input('Enter side AC:'))
    angle = float(input('Enter angle(AB,AC):'))
    main(side_a, side_b, angle)