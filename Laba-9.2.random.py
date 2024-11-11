
from random import choice

matrix = []

for i in range(3):
   matrix.append([0] * 3)

   number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(3):
    for j in range(3):
        matrix[i][j] = choice(number)
        number.remove(matrix[i][j])

is_magic = True

for i in range(3):
    for j in range(3):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j])
    if row_sum == col_sum:
        is_magic = True
    elif row_sum != col_sum:
        is_magic = False
        break

diag_sum1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
diag_sum2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
if diag_sum1 != diag_sum2:
    is_magic = False

if diag_sum1 == diag_sum2 == row_sum == col_sum:


    print("Магический квадрат: ")
    for i in range(3):
     for j in range(3):
         print(matrix[i][j], end=" ")
    print()
else:
    print("Матрица не является магическим квадратом. Повторная генерация матрицы: ")
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = choice(number)
            number.remove(matrix[i][j])

    print("Hовая матрица: ")
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end= " ")
        print()
