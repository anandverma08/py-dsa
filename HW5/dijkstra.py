from queue import PriorityQueue  # essentially a binary heap


def dijkstra(G, start, goal):
    """ Uniform-cost search / dijkstra """
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()

    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get()  # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else:  # if todo ran out
            break  # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for neighbor, distance in G[vertex]:
            if neighbor in visited: continue  # skip these to save time
            old_cost = cost.get(neighbor, float('inf'))  # default to infinity
            new_cost = cost[vertex] + distance
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vertex

    return parent


def make_path(parent, goal):
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None:  # root has null parent
        path.append(v)
        v = parent[v]
    return path[::-1]


## Example

G = {  # random example graph
    's': {('t', 3),('y',5)},
    't': {('y', 2), ('x', 6)},
    'x': {('z', 2)},
    'z': {('x', 7), ('s', 3)},
    'y': {('x', 4), ('z', 6)},

}

parent = dijkstra(G, 'z', 's')
print(make_path(parent, 's'))