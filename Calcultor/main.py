x = input()
y = ""
try:
    str1 = compile(x, 'string', 'eval')
except SyntaxError:
    print("Выражение введено не верно")
    y = 1

try:
    print(eval(str1))
except ZeroDivisionError:
    print("На ноль не делится\nзакрываюсь")
except NameError:
    if y == 1:
        print("закрываюсь")
    else:
        print("Выражение введено не верно\nзакрываюсь")
