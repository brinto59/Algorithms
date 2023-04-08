# All pairs shortest path (Floyd - Warshall) - Dynamic Programming
import sys
infinity = sys.maxsize

A = [
    [0] * 5,
    [0, 0, 3, infinity, 7],
    [0, 8, 0, 2, infinity],
    [0, 5, infinity, 0, 1],
    [0, 2, infinity, infinity, 0]
]
vertex_no = 4

for k in range(1, vertex_no+1):
    for i in range(1, vertex_no + 1):
        for j in range(1, vertex_no + 1):
            A[i][j] = A[i][j] if A[i][j] < A[i][k] + A[k][j] else A[i][k] + A[k][j]

print(A)