"""Проверить, является ли введенное число четным"""


def check_int():
    num = input()
    while type(num) != int:
        try:
            return int(num)
        except Exception as e:
            print(f"Вы ввели строку, хотя ожидалось число. Ошибка: {e}")
        num = input()


print(check_int() % 2 == 0)
