"""
8. Відомо, що X кг цукерок коштують A гривень. Визначити, скільки коштує 1 кг і Y кг цих же
цукерок.
"""


def main(x: float, a: float, y: float):
    if x > 0 and y > 0 and a > 0:
        kg = round(a / x, 2)
        y = y * kg

        return f'Один кілограм цукерок коштує {kg} грн, а У кг коштують {y} грн'
    else:
        return f'Невірно введено дані'


if __name__ == '__main__':
    x_ = float(input('Ввдеіть Хкг цукерок: '))
    a_ = float(input('Введіть скільки коштує Х кг: '))
    y_ = float(input('Введіть скільки ви хочете купити кг цукерок: '))

    result = main(x_, a_, y_)
    print(result)
