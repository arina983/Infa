from itertools import count
from os.path import split

n = int(input("введите количество задач: "))
count_sol = 0
for _ in range(n):
    num = input().split()
    p = int(num[0])
    v = int(num[1])
    t = int(num[2])
    if p + v + t >= 2 :
        count_sol += 1
print(count_sol)