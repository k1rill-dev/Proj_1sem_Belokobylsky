s = input()
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
print(error_index)
