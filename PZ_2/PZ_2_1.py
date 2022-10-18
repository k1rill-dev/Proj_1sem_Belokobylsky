"""Известно что X кг шоколадных конфет стоит А рублей, а Y кг
 ирисок стоит В рублей. Определить сколько стоит 1 кг шоколадных конфет,
 1кг ирисок, а также во сколько раз шоколадные конфеты дороже
 ирисок"""


def check_fl(str):
    num = input(str)
    while type(num) != float:
        try:
            return float(num)
        except Exception as e:
            print(f"Вы ввели строку, хотя ожидалось число. Ошибка: {e}")
        num = input(str)


chocolate_candy_mass = check_fl("введите массу шок. конфет: ")
chocolate_candy_price = check_fl("введите стоимость конфеток: ")
iris_mass = check_fl("введите массу ирисок: ")
iris_price = check_fl("введите стоимость конфет: ")
chocolate_candy_1kg_price = chocolate_candy_price / chocolate_candy_mass
iris_1kg_price = iris_price / iris_mass
print(
    f"1кг шоколадных конфет стоит: {round(chocolate_candy_1kg_price, 3)}, 1кг ирисок стоит: {round(iris_1kg_price, 3)}, шоколадные конфеты дороже ирисок в {(chocolate_candy_1kg_price / iris_1kg_price) * 100}%")
