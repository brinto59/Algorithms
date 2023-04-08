# Multistage graph - Dynamic Programming
import sys
infinity = sys.maxsize

vertex = 12
stages = 4
c = [
    [0]*13,
    [0, 0, 9, 7, 3, 2, *[infinity] * 7],
    [0, infinity, 0, *[infinity]*3, 4, 2, 1, *[infinity]*4],
    [0, infinity, infinity, 0, infinity, infinity, 2, 7, *[infinity]*5],
    [0, *[infinity]*3, 0, *[infinity]*3, 11, *[infinity]*4],
    [0, *[infinity]*4, 0, infinity, 11, 8, *[infinity]*4],
    [0, *[infinity]*5, 0, infinity, infinity, 6, 5, *[infinity]*2],
    [0, *[infinity]*6, 0, infinity, 4, 3, infinity, infinity],
    [0, *[infinity]*7, 0, infinity, 5, 6, infinity],
    [0, *[infinity]*8, 0, infinity, infinity, 4],
    [0, *[infinity]*9, 0, infinity, 2],
    [0, *[infinity]*10, 0, 5],
    [0, *[infinity]*11, 0]
]
cost = [0] * (vertex + 1)  # cost from every vertex to the end vertex
d = [0] * (vertex + 1)  # the vertex giving the minimum cost in every vertex
path = [0] * (stages + 1)  # the shortest path through vertices
minimum = 0

d[vertex] = 12

for i in range(vertex - 1, 0, -1):
    minimum = infinity
    for j in range(i+1, vertex + 1):
        if c[i][j] != 0 and c[i][j] + cost[j] < minimum:
            minimum = c[i][j] + cost[j]
            d[i] = j
    cost[i] = minimum

path[1] = 1
path[stages] = vertex
for i in range(2, stages):
    path[i] = d[path[i-1]]


print(cost)
print(d)