"""Функция mean, вычисляющая среднее арифмитическое
и среднее геометрическое двух введенных чисел"""

from math import sqrt

from PZ_3.PZ_3_0 import check_int


def mean(x, y):
    print(f"среднее арифмитическое: {(x + y) / 2}")
    print(f"среднее геометрическое: {sqrt(x * y)}")


def main():
    a, b, c, d = check_int(), check_int(), check_int(), check_int()
    mean(a, b)
    mean(a, c)
    mean(a, d)

#комментарий
if __name__ == "__main__":
    main()
