import sys
from pprint import pprint
matrix = [list(map(int, x.strip().split())) for x in sys.stdin.readlines()]
out = []
column_index = len(matrix[0]) - 2
for i in range(len(matrix)):
    out += [matrix[i][column_index]]
mn = min(out)
for i in range(len(matrix)):
    if matrix[i][column_index] == mn:
        matrix[i][column_index] = 0
        break

pprint(matrix)