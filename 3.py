import sys

matrix = [list(map(int, x.strip().split())) for x in sys.stdin.readlines()]
out = []
for i in range(len(matrix[3])):
    if matrix[3][i] % 7 == 0 and matrix[3][i] % 2!= 0:
        out += [(3, i)]
print(*out)