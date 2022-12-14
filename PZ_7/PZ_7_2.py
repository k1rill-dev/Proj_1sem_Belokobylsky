"""Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
расставлены правильно (то есть каждой открывающей соответствует одна
закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
в которой расположена первая ошибочная закрывающая скобка, или, если
закрывающих скобок не хватает, число — 1."""

s = input("Введите строку, содержащую латинские буквы и круглые скобки: ")
a = 0
error_index = 0
for x, i in enumerate(s):
    if i == "(":
        a += 1
    elif i == ")":
        a -= 1
    if a < 0:
        error_index = x
        break

print(-1 if a > 0 else error_index)
