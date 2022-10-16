import timeit


def output(a):
    print("Результат операции:")
    for i in a:
        for j in i:
            print(j, end=" ")
        print()


def trans(a):
    b = [[0 for i in range(3)] for i in range(3)]

    for i in range(3):
        for j in range(3):
            b[j][i] = a[i][j]
    return b


def muliply(a, b):
    for i in range(3):
        for j in range(3):
            b[i][j] *= a
    return b


def opred(a):
    return (a[0][0] * a[1][1] * a[2][2] +
            a[0][1] * a[1][2] * a[2][0] +
            a[1][0] * a[2][1] * a[0][2] -
            (a[2][0] * a[1][1] * a[0][2] +
             a[1][0] * a[0][1] * a[2][2] +
             a[2][1] * a[1][2] * a[0][0]))


def algdop(a):
    b = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            c = list()
            for i1 in range(3):
                if i1 == i:
                    continue
                c1 = list()
                for j1 in range(3):
                    if j1 == j:
                        continue
                    c1.append(a[i1][j1])
                c.append(c1)
            b[i][j] = (-1) ** (i + j) * (c[0][0] * c[1][1] - c[0][1] * c[1][0])
    return b


def inv(a):
    return muliply(1 / opred(a), trans(algdop(a)))


a = list()
print("Введите матрицу: ")
for i in range(3):
    a.append(list(map(int, input().split())))
if opred(a) == 0:
    print("Нельзя вычислить обратную матрицу")
else:
    print("Обратная матрица: ")
    output(inv(a))

print(timeit.timeit('inv(a)', number=100000, globals=globals()))