f1 = 1
f2 = 1
n = int(input("Введи число: "))
i = 0

while i < n-2:
    f_summ = f1 + f2
    f1 = f2
    f2 = f_summ
    i+= 1
print(f2)