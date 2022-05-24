"""
    2. Дана сторона квадрата a. Знайти його площу S=a2
"""


def main(fside: float):
    if fside > 0:
        return f'Square = {side ** 2}'
    else:
        return'Error'


if __name__ == '__main__':
    side = float(input("Enter side of square: "))
    result = main(side)
    print(result)