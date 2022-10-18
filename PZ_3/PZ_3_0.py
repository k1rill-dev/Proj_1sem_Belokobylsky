def check_int():
    num = input()
    while type(num) != int:
        try:
            return int(num)
        except Exception as e:
            print(f"Вы ввели строку, хотя ожидалось число. Ошибка: {e}")
        num = input()


def first_task():
    a = check_int()
    b = check_int()
    if a * b < 0:
        print((a * b) * 8)
    else:
        print((a * b) * 1.5)


def second_task():
    a = check_int()
    if a % 2 == 0:
        print(a / 4)
    else:
        print(a * 5)


def third_task():
    a = check_int()
    # print(a//10, a % 10)
    if ((a // 10) + (a % 10)) % 2 == 0:
        print(a + 2)
    else:
        print(a - 2)


def fourth_task():
    a = check_int()
    if a > 0:
        print(a + 20)
    else:
        print(a - 5)


def fifth_task():
    a = check_int()
    b = check_int()
    if (a + b) % 5 == 0:
        print(a + b + 1)
    else:
        print(a + b - 2)


def main():
    first_task()
    second_task()
    third_task()
    fourth_task()
    fifth_task()


if __name__ == "__main__":
    main()
