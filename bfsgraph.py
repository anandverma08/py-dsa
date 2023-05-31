def bfs(graph, start):
    visited_edges = set()  # to keep track of visited edges
    visited_vertices = set()  # to keep track of visited vertices
    queue = [start]  # to store the vertices to visit next

    while queue:
        # Dequeue a vertex from the front of the queue
        vertex = queue.pop(0)

        # If the vertex has not been visited yet, mark it as visited and add its neighbors to the queue
        if vertex not in visited_vertices:
            visited_vertices.add(vertex)
            neighbors = graph[vertex]
            for neighbor in neighbors:
                # Check if the edge has been visited before
                    if ( (vertex, neighbor) and (neighbor, vertex) ) not in visited_edges:
                    # Mark the edge as visited and add the neighbor to the queue
                    visited_edges.add((vertex, neighbor))
                    # visited_edges.add((neighbor, vertex))
                    queue.append(neighbor)

    return visited_edges


# Example usage
graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3]
}

start_vertex = 1
visited_edges = bfs(graph, start_vertex)
print("Visited edges:", visited_edges)