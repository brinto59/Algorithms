# Depth First Search
selected_edges = []


def back_edges(graph, selected_edges):
    backedges = []
    for i in range(len(graph)):
        flag = True
        for j in range(len(selected_edges)):
            if ((graph[i][0] == selected_edges[j][0] and graph[i][1] == selected_edges[j][1]) or (graph[i][0] == selected_edges[j][1] and graph[i][1] == selected_edges[j][0])):
                flag = False
        if flag and graph not in backedges:
            backedges.append(graph[i])
    return backedges


def connected_vertices(graph, vertex, visited_vertices):  # have to be directed
    connected = []
    for i in range(len(graph)):
        if vertex in graph[i]:
            if vertex == graph[i][0] and graph[i][1] not in visited_vertices:
                connected.append(graph[i][1])
            elif vertex == graph[i][1] and graph[i][0] not in visited_vertices:
                connected.append(graph[i][0])

    return connected


def main():
    vertices_no = 10
    edges = [[4, 1], [1, 2], [4, 3], [2, 3], [3, 10], [9, 3], [2, 7], [5, 2], [8, 2], [5, 6], [5, 7], [7, 8], [5, 8]]
    # edges = [[1, 2], [4, 1], [5, 1], [2, 3], [2, 6], [7, 2]]
    # edges = [[1, 2], [3, 1], [2, 4], [2, 5], [3, 6], [3, 7]]
    vertex = 1  # source vertex
    stack = []
    stack_index = 0
    selected_vertices = [vertex]
    connected_edges = []
    for i in range(vertices_no+1):
        connected_edges.append([])

    connected = connected_vertices(edges, vertex, selected_vertices)
    connected_edges[vertex] = connected

    for j in range(2 * (vertices_no-1)):
        selected_flag = False
        if len(connected_edges[vertex]) != 0:
            previous_vertex = vertex

            # selecting next vertex that is not already selected
            for k in range(len(connected_edges[previous_vertex])):
                if connected_edges[previous_vertex][k] not in selected_vertices:
                    vertex = connected_edges[previous_vertex][k]
                    selected_flag = True
                    break

            if selected_flag:
                connected_edges[previous_vertex].remove(vertex)
                selected_edges.append([previous_vertex, vertex])
                selected_vertices.append(vertex)
                stack.append(previous_vertex)
                stack_index += 1
                connected_edges[vertex] = connected_vertices(edges, vertex, selected_vertices)
            else:
                vertex = stack[stack_index - 1]
                stack.pop(stack_index - 1)
                stack_index -= 1
        else:
            vertex = stack[stack_index-1]
            stack.pop(stack_index-1)
            stack_index -= 1
    print(selected_vertices)
    print(selected_edges)
    print(back_edges(edges, selected_edges))


if __name__ == "__main__":
    main()