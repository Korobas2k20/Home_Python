#написать программу для поиска треугольника
a = input("Введите сторону A: ") 
b = input("Введите сторону B: ")
c = input("Введите сторону C: ")

if (a+b) > c and (a+c) > b and (b+c)>a:
    print("Такой треугол есть")
else:
    print("Такой треугол нема")