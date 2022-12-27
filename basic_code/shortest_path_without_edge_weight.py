class Data:
    def __init__(self, node_name, path_length):
        self.node_name = node_name
        self.path_length = path_length

    def __str__(self):
        return f"node {self.node_name} path length {self.path_length}"

class Node:
    def __init__(self, node_name, path_length):
        self.data = Data(node_name, path_length)
        self.next = None

class Queue:
    """
    enqueue(data): add node to the rear
    deque(): remove node from the front

    front-> node -> node > node -> ... -> rear
    """
    def __init__(self):
        self.front = None
        self.rear = None
    
    # O(1)
    def enqueue(self, node_name, path_length):
        node = Node(node_name, path_length)
        if self.rear == None: # first time adding a node
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    # O(1)
    def deque(self):
        if self.front == None:
            return None

        temp = self.front
        data = self.front.data

        self.front = self.front.next
        if self.front == None: # no node left
            self.rear = None

        del temp
        return data

    # O(1)
    def isEmpty(self):
        return self.front == None

    def print(self):
        if self.isEmpty():
            print("Queue is empty\n")
        else:
            node = self.front
            print("front", end="->")
            while(node):
                print(str(node.data), end="->")
                node = node.next
            print("None", end="\n")

def shortest_path(graph, source, destination):
    visited = set()
    queue = Queue()
    queue.enqueue(source, path_length = 0)

    while(not queue.isEmpty()):
        # queue.print()
        current = queue.deque()

        if current.node_name == destination:
            # print(f"destination found! {current.node_name} {current.path_length}")
            return current.path_length

        # print(f"node {current.node_name} {current.path_length}")
        visited.add(current.node_name)

        for adj in graph[current.node_name]:
            if adj not in visited:
                queue.enqueue(adj, current.path_length + 1) # without edge weight, only count edge

    return -1 # not reachable from source to destination

graph = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

path_length = shortest_path(graph, source = 'i', destination = 'm')
print(f"destination path_length {path_length}")