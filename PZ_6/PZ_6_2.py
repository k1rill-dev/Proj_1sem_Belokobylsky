"""Дан список размера N. Найти номера тех элементов список, которые больше своего
левого соседа, и количество таких элементов. Найденные номера выводить в порядке их убывания.
"""
import random

# (lambda a: print(len(a), a))(
#     list(map(lambda x: x[0], filter(lambda x: x[1], enumerate(list(map(lambda x: n[n.index(x) - 1] < x, n)))))))

n, result, a = list(), list(), list()
try:
    for i in range(random.randint(0, 100)):
        n.append(random.randint(0, 100))
    for i in n:
        a.append(n[n.index(i) - 1] < n[n.index(i)])
    for i in list(filter(lambda x: x[1], list(enumerate(a)))):
        result.append(i[0])
except Exception as e:
    print(f"Произошла ошибка - {str(e)}")

print(f"Номера - {result}, количество - {len(result)}")
