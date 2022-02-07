import sys

matrix = [list(map(int, x.strip().split())) for x in sys.stdin.readlines()]
transpose_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
out = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose_matrix[j][i] = matrix[i][j]


print(sum(max(x) for x in transpose_matrix))