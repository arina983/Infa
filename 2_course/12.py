a,b = list(map(int, input("введите вес Лимака и Боба: ").split()))
if a > b:
    print("вес Лимака должен быть меньше веса Боба!!!")
    exit()

count = 0

while a <= b:
    a += a * 3
    b += b * 2
    count += 1
print(count)