"""Дан список размера N. Обнулить элементы списка, расположенные между его
минимальным и максимальным элементами (не включая минимальный и максимальный элементы)."""
import random

n = []
for i in range(random.randint(1, 100)):
    n.append(random.randint(1, 100))

# (lambda a, b: print(list(map(lambda x: 0 if a < n.index(x) < b else x, n))))(n.index(min(n)), n.index(max(n)))
# print(list(map(lambda x: 0, n[min(n):max(n)])))
result = list()
for i in n[min(n):max(n)]:
    i = 0
    result.append(i)
print(result)