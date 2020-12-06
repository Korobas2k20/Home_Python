a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = str(input("Выберите действие(+-/*): "))

if c == "+":
    a = a + b
    print("Ваше число:",a)
elif c == "-":
    a = a - b
    print("Ваше число:",a)
elif c == "/":
    a = a / b
    print("Ваше число:",a)
elif c == "*":
    a = a * b
    print("Ваше число:",a)
else:
    print("Я не знаю эту операцию!")