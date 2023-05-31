import math

# Reading from ContactList.txt and preparing the contact Graph
f = open("ContactList.txt", "r")
data = f.readlines()
contact_Graph = []
for i in range(0, len(data)):
    contact_Graph.append({
        "id": int(data[i].split(" ")[0]),
        "start": float(data[i].split(" ")[1]),
        "end": float(data[i].split(" ")[2]),
        "sender": int(data[i].split(" ")[3]),
        "receiver": int(data[i].split(" ")[4]),
        "owlt": float(data[i].split(" ")[5]),
        "arr_time": math.inf,
        "pred": None,
        "visited": False,
        "visited_n": set()
    })

# Initializing contact_root
c_root = {
    "id": 1,
    "start": 0,
    "end": math.inf,
    "sender": 1,
    "receiver": 1,
    "owlt": 0,
    "arr_time": 0,
    "pred": None,
    "visited": False,
    "visited_n": set([1])
}


class PriorityQueue:
    def __init__(self):
        self.heap = []

    # checking if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Pushing the element in the priority queue, priority being arr_time
    def push_queue(self, priority, item):
        self.heap.append((priority, item))
        self.shift_up_queue(len(self.heap) - 1)

    # Popping the element from the queue
    def pop_queue(self):
        if len(self.heap) == 0:
            return None
        # Popping the first element from the heap
        priority, element = self.heap[0]

        # Taking last element of the queue and placing it at first position
        # Pushing queue one step down
        last_priority, last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = (last_priority, last_element)
            self.shift_down_queue(0)
        return element

    # Shifting the element up if its arrival time is less than parent's arrival time
    def shift_up_queue(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.shift_up_queue(parent_index)


    # Takes an index and shift it down maintaining the minimim heap property
    def shift_down_queue(self, index):
        l_child = index * 2 + 1
        r_child = index * 2 + 2
        minimum = index

        # finding the minimum element and checking if its equal to the index
        if l_child < len(self.heap) and self.heap[l_child][0] < self.heap[minimum][0]:
            minimum = l_child
        if r_child < len(self.heap) and self.heap[r_child][0] < self.heap[minimum][0]:
            minimum = r_child
        # if minimum is not equal to index, swap both of them and call shift_down_queue on minimum
        if minimum != index:
            self.heap[index], self.heap[minimum] = self.heap[minimum], self.heap[index]
            self.shift_down_queue(minimum)


def CGR(Graph, c_root, c_dest):
    route = []
    c_final = {}
    BDT = math.inf
    c_current = c_root

    while True:
        # find potential neighbours for every c_current node
        (c_final, BDT) = CRP(Graph, c_current, c_final, BDT, c_dest)

        # finding the minimum from the potential neighbours
        c_next = CSP(Graph, BDT, c_current)
        print(c_next)

        # Moving c_current to next minimum neighbour
        if c_next is not None:
            c_current = c_next
        else:
            break

    # tracking back from Destination to Source and appending it to route
    while c_final["pred"] is not None:
        route.append(c_final["id"])
        c_final = c_final["pred"]

    # Returning Route and BDT
    return route[::-1], BDT


def CSP(Graph, BDT, current):
    # Initializing Priority Queue
    priority_queue = PriorityQueue()
    # looping over all the contacts in graph
    for i in range(0, len(Graph)):

        # Skipping if arriving time of a contact if greater than BDT or the contact is already visited
        if Graph[i]["arr_time"] > BDT or Graph[i]["visited"] == True:
            continue

        # checking if the sender of the next contact is same as current's receiver and arrival time of current is
        # less than contact's end time, if yes, pushing in priority queue
        elif Graph[i]["sender"] == current["receiver"] and (current["arr_time"] < Graph[i]["end"]):
            priority_queue.push_queue(Graph[i]["arr_time"], Graph[i])

    if priority_queue.is_empty():
        return None

    # popping from priority queue, returning lowest arrival time value
    return priority_queue.pop_queue()


def CRP(Graph, c_current, c_final, BDT, c_dest):
    # looping over all the contacts and searching for potential neighbours
    for i in range(0, len(Graph)):

        if Graph[i]["sender"] == c_current["receiver"]:

            # Skipping contact if the arrival time is later than the end time, or its already visited
            if Graph[i]["end"] < c_current["arr_time"] or Graph[i]["visited"] == True or Graph[i]["receiver"] in \
                    c_current["visited_n"]:
                continue

            arr_time = max(c_current["arr_time"], Graph[i]["start"]) + Graph[i]["owlt"]

            # setting arrival time and predecessor for all neighbours
            if arr_time < Graph[i]["arr_time"]:
                Graph[i]["arr_time"] = arr_time
                Graph[i]["pred"] = c_current
                Graph[i]["visited_n"] = c_current["visited_n"].union({Graph[i]["receiver"]})

                # if potential neighbour is the destination, assigning BDT and final contact
                if Graph[i]["receiver"] == c_dest and Graph[i]["arr_time"] < BDT:
                    BDT = Graph[i]["arr_time"]
                    c_final = Graph[i]

    # marking the current node as visited
    c_current["visited"] = True
    return c_final, BDT


optimal_path, BDT = CGR(contact_Graph, c_root, 12)

print("Optimal Path :", optimal_path)
print("BDT :", BDT)


