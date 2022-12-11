"""Дан список размера N. Найти номера тех элементов список, которые больше своего
левого соседа, и количество таких элементов. Найденные номера выводить в порядке их убывания.
"""
import random

n, res = list(), list()
try:
    for i in range(random.randint(3, 10)):
        n.append(random.randint(0, 10))
    print(n)
    for index, value in enumerate(n):
        if n[index - 1] < n[index]:
            print(value)
            res.append(index)

except Exception as e:
    print(f"Произошла ошибка - {str(e)}")

print(f"Номера - {list(reversed(res))}, количество - {len(res)}")
