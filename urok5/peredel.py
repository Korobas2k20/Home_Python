a = int(input("Введите ваше число: "))
b = " "

while a > 0:
    b = str(a % 2) +b
    a = a // 2
print(b)