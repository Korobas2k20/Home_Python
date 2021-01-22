print("Калькулятор через функции")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите знак операции: ")

def Calc(a,b,c):
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a/b)
    else:
        print("I don't now this operation")
print(Calc(a,b,c))