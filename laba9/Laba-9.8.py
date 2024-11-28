n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
A = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
     A[0][i] = 1
for j in range(m):
     A[0][j] = 1

for i in range(0, n):
    for j in range(0, m):
        A[i][j] = A[i-1][j] + A[i][j-1]

for i in range(n):
    for j in range(m):
     print(f"{A[i][j]:6d}", end="")
    print() 
