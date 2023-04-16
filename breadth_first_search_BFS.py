# Breadth First Search
cross_edges = []
selected_edges = []


def connected_vertices(graph, vertex, visited_vertices):  # have to be directed
    connected = []
    for i in range(len(graph)):
        if vertex in graph[i]:
            if vertex == graph[i][0]:
                if graph[i][1] not in visited_vertices:
                    connected.append(graph[i][1])
                    selected_edges.append(graph[i])
                elif graph[i] not in selected_edges and graph[i] not in cross_edges:
                    cross_edges.append(graph[i])
            elif vertex == graph[i][1]:
                if graph[i][0] not in visited_vertices:
                    connected.append(graph[i][0])
                    selected_edges.append(graph[i])
                elif graph[i] not in selected_edges and graph[i] not in cross_edges:
                    cross_edges.append(graph[i])
    return connected


def main():
    vertices_no = 10
    # edges = [[1, 2], [4, 1], [5, 1], [2, 3], [2, 6], [7, 2]]
    edges = [ [4, 1], [1, 2], [4, 3], [2, 3], [3, 10], [9, 3], [2, 7], [5, 2], [8, 2], [5, 6], [5, 7], [7, 8], [5, 8]]
    source_vertex = 1
    queue = [source_vertex]
    connected = connected_vertices(edges, source_vertex, queue)
    queue.extend(connected)

    for i in range(1, vertices_no):
        connected = connected_vertices(edges, queue[i], queue)
        queue.extend(connected)

    print(queue)
    print(cross_edges)


if __name__ == "__main__":
    main()