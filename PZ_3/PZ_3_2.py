"""Определить процент вклада по размеру внесенного
депозита"""

def check_int(str):
    num = input(str)
    while type(num) != int:
        try:
            return int(num)
        except Exception as e:
            print(f"Вы ввели строку, хотя ожидалось число. Ошибка: {e}")
        num = input(str)

enter_sum = check_int("Введите сумму депозита:")

if enter_sum < 50000:
    print("Ваш процент равен 4")
elif 50000 < enter_sum < 100000:
    print("Ваш процент равен 5")
elif 100000 < enter_sum < 150000:
    print("Ваш процент равен 6")
elif 150000 < enter_sum < 200000:
    print("Ваш процент равен 7")
else:
    print("В вашем случае лучше обратиться в банк лично и узнать процент там")
