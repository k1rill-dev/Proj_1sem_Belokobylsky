"""Выводятся числа в диапазоне A&B в порядке убывания
и их количество"""

from PZ_3.PZ_3_0 import check_int

a = check_int()
b = check_int()
count = 0

for i in reversed(range(a, b+1)):
    count += 1
    print(i)

print(count)
