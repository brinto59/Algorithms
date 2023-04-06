# Prim's Algorithm
import math


# disjoint set
class Disjointset:
    def __init__(self, no_of_vertices):
        self.array_of_vertices = []
        self.no_of_vertices = no_of_vertices
        self.makeset()

    def makeset(self):
        for i in range(self.no_of_vertices):
            self.array_of_vertices.append(-1)

    def findcycle(self, vertice1, vertice2):
        if (self.array_of_vertices[vertice1-1] > 0 and self.array_of_vertices[vertice2-1] > 0) and (self.array_of_vertices[vertice1-1] == self.array_of_vertices[vertice2-1]):
            return True
        elif (self.array_of_vertices[vertice1-1] == vertice2) or (self.array_of_vertices[vertice2-1] == vertice1):
            return True
        else:
            return False

    def union(self, vertice1, vertice2):

        if self.array_of_vertices[vertice1-1] < 0:
            parent1 = vertice1
        else:
            parent1 = self.array_of_vertices[vertice1-1]

        if self.array_of_vertices[vertice2-1] < 0:
            parent2 = vertice2
        else:
            parent2 = self.array_of_vertices[vertice2-1]

        min_parent = parent2 if self.array_of_vertices[parent2-1] > self.array_of_vertices[parent1-1] else parent1  # parent with minimum child
        other_parent = parent1 if self.array_of_vertices[parent2-1] > self.array_of_vertices[parent1-1] else parent2

        for i in range(self.no_of_vertices):
            if self.array_of_vertices[i] == min_parent or i+1 == min_parent:
                self.array_of_vertices[i] = other_parent
                self.array_of_vertices[other_parent - 1] -= 1


# add vertice which are selected
def add_vertice(selected_vertices, num):
    if num[1][0] not in selected_vertices:
        selected_vertices.append(num[1][0])
    else:
        selected_vertices.append(num[1][1])

# find adjacent edges of the selected vertices
def adjacent_edges(graph, selected_vertices):
    possible_edges = []
    for i in range(len(selected_vertices)):
        for j in range(len(graph)):
            if selected_vertices[i] in graph[j][1]:
                possible_edges.append(graph[j])
    # print(possible_edges)
    return possible_edges


# heapify - min heap - for graph
def heapify(array):
    length = len(array)
    parent = length
    for i in range(length):
        if 2*parent+1 <= length:
            if array[2*parent][0] < array[2*parent-1][0] and array[2*parent][0] < array[parent-1][0]:
                array[2*parent], array[parent-1] = array[parent-1], array[2*parent]
            elif array[2*parent-1][0] <= array[2*parent][0] and array[2*parent - 1][0] < array[parent-1][0]:
                array[2 * parent - 1], array[parent - 1] = array[parent - 1], array[2 * parent - 1]
        elif 2*parent <= length:
            if array[2*parent - 1][0] < array[parent - 1][0]:
                array[2 * parent - 1], array[parent - 1] = array[parent - 1], array[2 * parent - 1]
        parent -= 1

    # print(array)
    return array[0]


if __name__ == "__main__":
    graph = [[28, [1, 2]], [16, [2, 3]], [12, [3, 4]], [22, [4, 5]], [25, [5, 6]], [10, [6, 1]], [24, [5, 7]],
             [14, [2, 7]], [18, [4, 7]]]
    # graph = [[6, [1, 2]], [5, [2, 3]], [3, [3, 5]], [2, [5, 4]], [4, [1, 4]], [4, [4, 3]]]
    vertices = 7
    selected_vertices = []

    setObj = Disjointset(vertices)   # made a set with 7 vertices
    first_selected = heapify(graph)  # gives the minimum edge

    length = len(graph)
    minimum_cost = first_selected[0]
    selected_vertices.extend(first_selected[1])
    setObj.union(*first_selected[1])
    graph.remove(first_selected)

    for i in range(len(graph)-1):
        next_edge = heapify(adjacent_edges(graph, selected_vertices))
        graph.remove(next_edge)
        add_vertice(selected_vertices, next_edge)
        if setObj.findcycle(*next_edge[1]) is False:
            setObj.union(*next_edge[1])
            minimum_cost += next_edge[0]

    print(minimum_cost)

