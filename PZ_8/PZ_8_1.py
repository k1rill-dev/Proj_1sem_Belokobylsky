"""Дана строка «Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4». Преобразовать
информацию из строки в словарь, найти среднее арифметическое оценок,
результаты вывести на экран."""

string = "Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4"

print({
    'Фамилия': string.split()[0],
    'Имя': string.split()[1],
    'Группа': string.split()[2],
    'Оценки': string.split()[3:]
},
    f'Среднее арифмитическое оценок: {sum(list(map(int, string.split()[3:]))) / len(list(map(int, string.split()[3:])))}')