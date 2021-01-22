print("Программа для вычесления високосного года")
y = int(input("Введите год: "))

def year(y):
    if y % 4 == 0:
        return("Високосный код")
    else:
        return("Нет")
print(year(y))