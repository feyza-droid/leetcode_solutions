class Node:
    def __init__(self, data):
        self.data = data
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
    def enqueue(self, data):
        node = Node(data)
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

def bfs(graph, source, visited):
    queue = Queue()
    queue.enqueue(source)

    while(not queue.isEmpty()):
        current = queue.deque()
        print(f"node {current}")
        visited.add(current)

        for adj in graph[current]:
            if adj not in visited:
                queue.enqueue(adj)

graph = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

bfs(graph, source = 'i', visited = set()) # pick any node as the starting node
print("\n")
bfs(graph, source = 'o', visited = set()) # pick any node as the starting node