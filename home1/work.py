a = input("Введите имя файла: ")

if a.endswith(".html") or a.endswith(".htm") or a.endswith(".php"): #C:\DOC\САЙТ\index.html
    print("Это веб-страница!")
elif a.endswith(".doc") or a.endswith(".docx"):
    print("Это документ Word!")
elif a.endswith(".xls") or a.endswith(".xlsx"):
    print("Это документ Excel!")
elif a.endswith(".zip") or a.endswith(".rar") or a.endswith(".7z"):
    print("Это архив!")
elif a.endswith(".exe"):
    print("Это программа!")
else:
    print("Это что-то вообще другое!")