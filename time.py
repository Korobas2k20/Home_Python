print("Программа для нахождения временни")
y = int(input("Введите ваши секунды: "))

def Time(y):
    hours = y // 3600
    minute = y // 60 % 60
    second = y % 60
    print(hours,":",minute,":",second, sep="")
print(Time(y))