n = int(input("Введите размер матрицы: "))
matrix = []

print("Введите элементы матрицы по строкам: ")
for _ in range(n):
    row_str = input()
    row = list(map(int, row_str.split()))
    matrix.append(row)

matrix[0][0], matrix[0][2], matrix[2][0], matrix[2][2] = matrix[2][0], matrix[2][2], matrix[0][0], matrix[0][2]

print("Измененная матрица: ")
for row in matrix:
    print(*row)