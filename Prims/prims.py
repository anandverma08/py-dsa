import math
import sys
import heapq
#
# class Graph():
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]
#                       for row in range(vertices)]
#
#     # A utility function to print
#     # the constructed MST stored in parent[]
#     def printMST(self, parent):
#         print("Edge \tWeight")
#         for i in range(1, self.V):
#             print(parent[i]+1, "-", i+1, "\t", self.graph[i][parent[i]])
#
#     # A utility function to find the vertex with
#     # minimum distance value, from the set of vertices
#     # not yet included in shortest path tree
#     def minKey(self, key, mstSet):
#
#         # Initialize min value
#         min = sys.maxsize
#
#         for v in range(self.V):
#             if key[v] < min and mstSet[v] == False:
#                 min = key[v]
#                 min_index = v
#
#         return min_index
#
#     # Function to construct and print MST for a graph
#     # represented using adjacency matrix representation
#
# # Driver's code
# if __name__ == '__main__':
#     g = Graph(6)
#     g.graph = [[0, 4, 0, 9, 0, 0],
#                [4, 0, 5, 2, 3, 1],
#                [0, 5, 0, 0, 0, 3],
#                [9, 2, 0, 0, 2, 0],
#                [0, 3, 0, 2, 0, 5],
#                [0, 1, 3, 0, 5, 0]
#                ]
#
#     g.prim()


def prim(graph):
    # Initialize the variables
    num_vertices = len(graph)
    key = [sys.maxsize] * num_vertices
    parent = [None] * num_vertices
    visited = [False] * num_vertices
    queue = []

    # Start from the first vertex
    start_vertex = 0
    key[start_vertex] = 0
    heapq.heappush(queue, (0, start_vertex))

    while queue:
        # Get the vertex with the smallest weight
        weight, vertex = heapq.heappop(queue)

        # Mark the vertex as visited
        visited[vertex] = True

        # Explore the neighbors of the vertex
        for neighbor in range(num_vertices):
            if graph[vertex][neighbor] != 0 and not visited[neighbor]:
                neighbor_weight = graph[vertex][neighbor]
                if neighbor_weight < key[neighbor]:
                    # Update the key and parent
                    key[neighbor] = neighbor_weight
                    print("Iteration")
                    print(key[neighbor])
                    parent[neighbor] = vertex
                    print(parent[neighbor])

                    print("Spanning tree vertices:", [i+1 for i in range(num_vertices) if visited[i]])
                    print("---------")
                    # Push the new key and vertex onto the queue
                    heapq.heappush(queue, (neighbor_weight, neighbor))

    # Build the minimum spanning tree
    minimum_spanning_tree = []
    for vertex in range(1, num_vertices):
        minimum_spanning_tree.append((parent[vertex], vertex))

    return minimum_spanning_tree

print(prim([[0, 4, 0, 9, 0, 0],
        [4, 0, 5, 2, 3, 1],
        [0, 5, 0, 0, 0, 3],
        [9, 2, 0, 0, 2, 0],
        [0, 3, 0, 2, 0, 5],
        [0, 1, 3, 0, 5, 0]
    ]))