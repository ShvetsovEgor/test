import sys

matrix = [list(map(int, x.strip().split())) for x in sys.stdin.readlines()]
out = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] % 10 == 2 and i > j:
             out += [matrix[i][j]]

print(*out)