import random

# Задание № 1

n = int(input("Введите размер матрицы: "))
item = int(input("Введите количество элементов в матрице: "))

matrix_1 = []

matrix_2 = []

matrix_3 = []

for i in range(n):
    a = [random.randint(-100, 100) for _ in range(item)]
    matrix_1.append(a)
    b = [random.randint(-100, 100) for _ in range(item)]
    matrix_2.append(b)


for i in range(n):
    c = []
    for j in range(item):
        c.append(matrix_1[i][j] + matrix_2[i][j])
    matrix_3.append(c)


print("Матрица №1: ", matrix_1)
print()
print("Матрица №2: ", matrix_2)
print()
print("Матрица №2: ", matrix_3)
