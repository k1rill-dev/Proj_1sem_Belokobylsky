"""Дан список размера N. Обнулить элементы списка, расположенные между его
минимальным и максимальным элементами (не включая минимальный и максимальный элементы)."""

n = [12, 234, 54, 234, 564, 23]

(lambda a, b: print(list(map(lambda x: 0 if a < n.index(x) < b else x, n))))(n.index(min(n)), n.index(max(n)))

