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

def dfs(graph, source, visited):
    stack = Stack(source)

    while(stack.is_non_empty()):
        current = stack.pop()
        print(f"node {current}")
        visited.add(current)

        for adj in graph[current]:
            if adj not in visited:
                stack.push(adj)

graph = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

dfs(graph, source = 'i', visited = set()) # pick any node as the starting node
print("\n")
dfs(graph, source = 'o', visited = set()) # pick any node as the starting node