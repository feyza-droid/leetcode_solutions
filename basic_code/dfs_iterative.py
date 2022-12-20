class Stack:
    def __init__(self, source):
        self.stack = [source]

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        value = self.stack[-1] # last element
        self.stack = self.stack[:-1]  # remove last element
        return value

    def is_non_empty(self):
        return len(self.stack) != 0

def dfs(graph, source):
    stack = Stack(source)

    while(stack.is_non_empty()):
        current = stack.pop()
        print(f"node {current}")

        for adj in graph[current]:
            stack.push(adj)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
dfs(graph, source = 'a') # pick any node as the starting node