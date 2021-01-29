#угадай число
import random

lowdigit = 10 #нижняя граница
highdigit = 50 # верх
digit = 0 # pc digit

win = False # Our WIN | EeEeeEEEeeEeeEeEeEeE |
playgame = True # продолжается ли игра?
countinput = 0 # подсчёт попыток
x = 0
start_score = 10
score = 0 # текущее кол-во очков
max_score = 0 

#==========================================================

while playgame:
    digit = random.randint(lowdigit,highdigit) #Загадка число
    # print(f" Наша цифра {digit}")
    print("_"*30)
    countinput = 0 # счёт попыток
    score = start_score
    print("Всё, PC загадал числа, угадай его")
    #==========================================================
    while not win and score > 0: # цикл отвечает за 1 раунд
        print("_"*30)
        print(f"Заработано очков: {score}")
        print(f"Рекорд: {max_score}")
        x= "" # преобразование в строку
        while not x.isdigit(): #цикл отвечает за число
            x = input(f"Введите число от {lowdigit} до {highdigit}: ")
            if not x.isdigit():
                print("."*30 + "введите число!")
        x = int(x) # преобразование в цифру
        if x == digit:
            win = True # ПАБЕДАААА
        else:
            length = abs(x-digit) # модуль делты нашего числа и числа загадки
            if length < 3:
                print("Капец как горячо да емае")
            elif length < 5:
                print("Горячо но не так сильно")
            elif length < 10:
                print("Тепло как в Анапе")
            elif length < 15:
                print("Прохладно")
            elif length < 20:
                print("Холодно брррррр")
            else:
                print("Ты чёт вообще не в ту сторону пошёл")
            if countinput == 7:
                score -= 10
                if digit % 2 == 0:
                    print("Число чётное")
                else:
                    print("Число не чётное")
            elif countinput == 6:
                score -=8
                if digit % 3 == 0:
                    print("Число делится на 3")
                else:
                    print("Число не делится на 3")
            elif countinput == 5:
                score -=6
                if digit % 4 == 0:
                    print("Число делится на 4")
                else:
                    print("Число не делится на 4")
            elif countinput > 2 and countinput < 5:
                score -=2
                if x > digit:
                    print("Загаданное число меньше вашего")
                else:
                    print("Загаданное число больше вашего")
            score -= 5
        countinput +=1
    print("*"*40)
    if x == digit:
        print("Ты победил")
    else:
        print("У вас закончились очки")
    if input("Enter - Сыграть ещё, 0 - выход") == 0:
        playgame = False
    else:
        win = False