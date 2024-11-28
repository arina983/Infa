
n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))

matrix = []
print("Введите элементы матрицы по строкам: ")
for _ in range(n):
    row_str = input()
    row = list(map(int, row_str.split()))
    matrix.append(row)
transposed_matrix = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        transposed_matrix[j][i] = matrix[i][j]

print("Транспонированная матрица: ")
for row in transposed_matrix:
    print(*row)
