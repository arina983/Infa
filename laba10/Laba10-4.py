n = int(input("Введите количество популярных имен: "))
m = input("Введите пол(ж или м): ") 
if m == "ж": 
    with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file7.txt', encoding = "UTF-8") as file:
        names = []
        for l in file:
            name, popularity = l.strip().split()
            names.append(name)
            if len(names) == n:
             break
    print(*names, end=" ")            

if m == "м":
    with open('C:/Users/Ариша/OneDrive/Рабочий стол/lab10/file8.txt', encoding = "UTF-8") as filee:
        namess = []
        for i in filee:
            namee, popularity = i.strip().split()
            namess.append(namee)
            if len(namess) == n:
             break
    print(*namess, end = " ")

