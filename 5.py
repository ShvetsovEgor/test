import sys

matrix = [list(map(int, x.strip().split())) for x in sys.stdin.readlines()]
mx = max([max(el) for el in matrix])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == mx:
            x, y = i, j
            break
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] < 0:
            matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]

print(matrix)