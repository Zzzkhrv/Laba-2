import numpy as np

def output(a):
    print("Результат операции:")
    for i in a:
        for j in i:
            print(j, end=" ")
        print()

a = list()
b = list()

action = int(input("Выберите действие(номер функции): \n"
                   "1. Транспонирование\n"
                   "2. Умножение матриц\n"
                   "3. Определение ранга\n"
                   ">>>>"))

if action == 1:
    n = int(input("Введите количество строк матрицы(возможные числа: 1 - 3): "))
    m = int(input("Введите количество столбцов матрицы(возможные числа: 1 - 3): "))

    print("Введите матрицу:")
    for i in range(n):
        a1 = list(map(int, input().split()))
        a.append(a1)
    a = np.array(a)
    output(np.transpose(a))

if action == 2:
    print("Первая матрица:")
    n = int(input("Введите количество строк матрицы(возможные числа: 1 - 3): "))
    m = int(input("Введите количество столбцов матрицы(возможные числа: 1 - 3): "))
    print("Введите матрицу:")
    for i in range(n):
        a1 = list(map(int, input().split()))
        a.append(a1)
    a = np.array(a)

    print('\nВторая матрица:')
    n1 = int(input("Введите количество строк матрицы(возможные числа: 1 - 3): "))
    while m != n1:
        n1 = int(input("Попробуйте снова: "))
    m1 = int(input("Введите количество столбцов матрицы(возможные числа: 1 - 3): "))
    print("Введите матрицу:")
    for i in range(n1):
        b1 = list(map(int, input().split()))
        b.append(b1)
    b = np.array(b)

    output(np.dot(a, b))

if action == 3:
    n = int(input("Введите количество строк матрицы(возможные числа: 2 - 3): "))
    m = int(input("Введите количество столбцов матрицы(возможные числа: 2 - 3): "))

    print("Введите матрицу:")
    for i in range(n):
        a1 = list(map(int, input().split()))
        a.append(a1)
    a = np.array(a)

    print("Результат:", np.linalg.matrix_rank(a))