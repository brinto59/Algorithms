# Kruskal's Algorithm
import math


# disjoint set
class Disjointset:
    def __init__(self, no_of_vertices):
        self.array_of_vertices = []
        self.no_of_vertices = no_of_vertices
        self.__makeset()

    def __makeset(self):
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


# min heap
def min_heap(graph):
    parent = 0
    for i in range(2, len(graph) + 1):
        for j in range(math.ceil(math.log2(len(graph)))):
            parent = math.floor(i / 2)
            if parent < 1:
                break
            if graph[i - 1][0] < graph[parent - 1][0]:
                graph[i - 1], graph[parent - 1] = graph[parent - 1], graph[i - 1]
                i = parent
            else:
                break
    # print(graph)


# min element - heap delete

def min_element(array, length_array):
    array[0], array[length_array-1] = array[length_array-1], array[0]
    length_array -= 1
    parent = 1
    if length_array < 1:
        return [array[length_array], length_array, array]
    for k in range(math.ceil(math.log2(length_array))):
        if 2*parent+1 <= length_array:
            if array[2*parent-1][0] < array[2*parent][0] and array[2*parent-1][0] < array[parent-1][0]:
                array[2*parent-1], array[parent-1] = array[parent-1], array[2*parent - 1]
                parent *= 2
            elif array[2*parent][0] <= array[2*parent-1][0] and array[2*parent][0] < array[parent-1][0]:
                array[2 * parent], array[parent - 1] = array[parent - 1], array[2 * parent]
                parent = 2*parent + 1
        elif 2*parent <= length_array:
            if array[2*parent-1][0] < array[parent-1][0]:
                array[2*parent-1], array[parent-1] = array[parent-1], array[2*parent - 1]
                parent = 2*parent
        else:
            break
    return [array[length_array], length_array, array]


if __name__ == "__main__":
    graph = [[28, [1, 2]], [16, [2, 3]], [12, [3, 4]], [22, [4, 5]], [25, [5, 6]], [10, [6, 1]], [24, [5, 7]],
             [14, [2, 7]], [18, [4, 7]]]
    vertices = 7
    setObj = Disjointset(vertices)   # made a set with 7 vertices
    min_heap(graph)  # sorted the graph ascending order
    length = len(graph)
    minimum_cost = 0

    for i in range(len(graph)):
        min_edge, length, graph = min_element(graph, length)
        if setObj.findcycle(*min_edge[1]) is False:
            setObj.union(*min_edge[1])
            minimum_cost += min_edge[0]

    print(minimum_cost)
