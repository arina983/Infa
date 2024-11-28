import random 

n = int(input("Введите секунду: "))
k = int(input("Введите коэффициент деления: "))
b = random.randint(0,4)

bacteria = 1

for _ in range(n):
    bacteria = k * bacteria + b

print("Количество бактерий после", n, "секунд:", bacteria)