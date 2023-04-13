# Travelling Salesman Problem using Dynamic Programming
# using recursive formula
import sys

n = 4
vertices = [1, 2, 3, 4]
source_vertex = 1
vertices.remove(source_vertex)
c = [
    [0]*5,
    [0, 0, 10, 15, 20],
    [0, 5, 0, 9, 10],
    [0, 6, 13, 0, 12],
    [0, 8, 8, 9, 0]
]


def g(s, vertices):
    minimum = sys.maxsize
    for k in range(0, len(vertices)):
        temp = [*vertices]
        temp.remove(vertices[k])
        if len(temp) == 0:
            val = c[s][vertices[k]] + c[vertices[k]][source_vertex]
        else:
            val = c[s][vertices[k]] + g(vertices[k], temp)
        if val < minimum:
            minimum = val
    return minimum


print(g(source_vertex, vertices))
