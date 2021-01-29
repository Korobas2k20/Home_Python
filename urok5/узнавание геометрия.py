print("guten Tag, 1 - прямоугольник, 2 - треугол, 3 - круг")
var = input("Что вы хотите выбрать?")

if var == "1":
    a = float(input("Введите размеры A:"))
    b = float(input("Введите размеры B:"))
    c = a*b
    print(c)
elif var == "2":
    b = float(input("Введите размеры b:"))
    h = float(input("Введите размеры h:"))
    c = float((1/2)*b*h)
    print(c)
elif var == "3":
    R = float(input("Введите радиус:"))
    P = 2*3.14*R
    print(P)
else:
    print("Я не знаю эту операцию")