"""
12. Дано значення кута α в градусах (0 ≤ α < 360). Обчислити значення цього ж кута в радіанах,
враховуючи, що 180 ° = π радіанів. У якості значення π використовувати 3.14.
"""


def main(angle):
    if 0 <= angle <= 360:
        radian = angle * 3.14 / 180
        return f'Radian = {radian}'
    else:
        return f'Error'


if __name__ == '__main__':
    ang_ = float(input('Enter the angle:'))
    result = main(ang_)
    print(result)