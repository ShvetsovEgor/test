import sys

matrix = [list(map(int, x.strip().split())) for x in sys.stdin.readlines()]
out = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] % 2 != 0:
             out += [matrix[i][j]]

print(sum(out) / len(out))