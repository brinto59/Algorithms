# Dijkstra's algorithm
# single source shortest path
import sys


def distance_from_source(graph, vertices, connected_vertices, source_vertex):
    vertices[source_vertex - 1][1] = 0
    for i in connected_vertices:
        vertices[graph[i][1][1] - 1][1] = graph[i][0]

    for j in range(len(vertices)):
        if vertices[j][1] == -1 and vertices[j][0] != source_vertex:
            vertices[j][1] = sys.maxsize


# directed connected vertice
def connected_vertice(graph, vertex, selected_vertices):  # have to be directed
    connected = []
    for i in range(len(graph)):
        if vertex == graph[i][1][0] and graph[i][1][1] not in selected_vertices:
            connected.append(i)  # index number of connected vertices in the graph
    return connected


def find_next_vertice(vertices, selected_vertices):
    next_vertices = []
    for i in range(len(vertices)):
        if vertices[i][0] not in selected_vertices:
            next_vertices.append(vertices[i])
    # print(heapify(graph, vertices), vertices, "hh")
    return heapify(next_vertices, len(next_vertices))


def heapify(vertices, length_of_vertices):
    if length_of_vertices < 1:
        return None
    parent = length_of_vertices
    for i in range(length_of_vertices):
        if 2 * parent + 1 <= length_of_vertices:
            if vertices[2 * parent][1] < vertices[2 * parent - 1][1] and vertices[2 * parent][1] < vertices[parent - 1][
                1]:
                vertices[2 * parent], vertices[parent - 1] = vertices[parent - 1], vertices[2 * parent]
            elif vertices[2 * parent - 1][1] <= vertices[2 * parent][1] and vertices[2 * parent - 1][1] < \
                    vertices[parent - 1][1]:
                vertices[2 * parent - 1], vertices[parent - 1] = vertices[parent - 1], vertices[2 * parent - 1]
        elif 2 * parent <= length_of_vertices:
            if vertices[2 * parent - 1][1] < vertices[parent - 1][1]:
                vertices[2 * parent - 1], vertices[parent - 1] = vertices[parent - 1], vertices[2 * parent - 1]
        parent -= 1

    # print(vertices)
    # vertices[0], vertices[length_of_vertices - 1] = vertices[length_of_vertices - 1], vertices[0]
    return vertices[0]


if __name__ == "__main__":
    # graph = [[2, [1, 2]], [1, [2, 3]], [4, [1, 3]], [3, [3, 5]], [7, [2, 4]], [1, [4, 6]], [5, [5, 6]], [2, [5, 4]]]  # directed graph

    graph = [[10, [1, 4]], [10, [4, 1]], [50, [1, 2]], [45, [1, 3]], [15, [2, 4]], [10, [2, 3]], [15, [4, 5]],
             [3, [6, 5]], [20, [5, 2]], [35, [5, 3]], [30, [3, 5]]]

    vertices = [[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [6, -1]]
    length_of_vertices = len(vertices)
    source_vertex = 1  # can be any vertice
    selected_vertices = [source_vertex]

    connected_vertices = connected_vertice(graph, source_vertex, selected_vertices)
    distance_from_source(graph, vertices, connected_vertices,
                         source_vertex)  # making which are not connected to infinity
    # print(vertices)

    temp_vertices = []
    for j in connected_vertices:
        temp_vertices.append(vertices[graph[j][1][1] - 1])

    length = len(temp_vertices)
    try:
        next_vertex = heapify(temp_vertices, length)
        selected_vertices.append(next_vertex[0])

        for i in range(len(graph)):
            connected_vertices = connected_vertice(graph, next_vertex[0], selected_vertices)
            for j in connected_vertices:
                if next_vertex[1] + graph[j][0] < vertices[graph[j][1][1] - 1][1]:
                    vertices[graph[j][1][1] - 1][1] = next_vertex[1] + graph[j][0]
            if length_of_vertices != len(selected_vertices):
                next_vertex = find_next_vertice(vertices, selected_vertices)
                selected_vertices.append(next_vertex[0])
            else:
                break

        print(graph)
        print(vertices)

    except Exception as error:
        print(vertices)





