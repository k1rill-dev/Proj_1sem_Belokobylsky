# string = input()
string = 'sdfas)fsdf(gsdgsdgsd)gasfdsadf'
if string.count(')') > 1:
    for i in enumerate(string):
        if i[1] == ')':
            print(i[0])
elif string.count(')') == 1 and string.count('(') == 1:
    print(0)
else:
    print(1)
