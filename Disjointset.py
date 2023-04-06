
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


def main():
    obj = Disjointset(8)
    print(obj.findcycle(2, 3))  # True if there is a cycle
    obj.union(2, 3)
    print(obj.array_of_vertices)
    print(obj.findcycle(2, 3))


if __name__ == "__main__":
    main()

# print(obj.findcycle(1, 3))
# obj.union(1, 3)
# print(obj.array_of_vertices)
#
# print(obj.findcycle(6, 7))
# obj.union(6, 7)
# print(obj.array_of_vertices)
#
# print(obj.findcycle(8, 7))
# obj.union(8, 7)
# print(obj.array_of_vertices)
#
# print(obj.findcycle(1, 8))
# obj.union(1, 7)
# print(obj.array_of_vertices)
#
# print(obj.findcycle(4, 5))
# obj.union(4, 5)
# print(obj.array_of_vertices)
#
# print(obj.findcycle(7, 5))
# obj.union(7, 5)
# print(obj.array_of_vertices)
#
# print(obj.findcycle(1, 5))



