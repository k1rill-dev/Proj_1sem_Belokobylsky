"""Сформировать и вывести целочисленный список размера 10, содержащий степени
двойки от первой до 10-й: 2, 4, 8,16, ...."""

# print(list(map(lambda x: 2 ** x, range(11))))
n = 0
result = []
try:
    while n < 11:
        result.append(2 ** n)
        n += 1
except Exception as e:
    print(f'Произошла ошибка - {str(e)}')

print(result)
