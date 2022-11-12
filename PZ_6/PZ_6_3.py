"""Дан список размера N. Обнулить элементы списка, расположенные между его
минимальным и максимальным элементами (не включая минимальный и максимальный элементы)."""
# (lambda a, b: print(list(map(lambda x: 0 if a < n.index(x) < b else x, n))))(n.index(min(n)), n.index(max(n)))
# print(list(map(lambda x: 0, n[min(n):max(n)])))
import random

n = []
for i in range(random.randint(1, 100)):
    n.append(random.randint(1, 100))

min_index = n.index(min(n))
max_index = n.index(max(n))
for i in range(len(n)):
    if min_index < i < max_index:
      n[i] = 0
print(n)
