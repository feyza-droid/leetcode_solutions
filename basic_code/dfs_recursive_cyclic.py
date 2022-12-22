def dfs(graph, source, visited):    
    print(f"node {source}")
    visited.add(source)

    for adj in graph[source]:
        if adj not in visited:
            dfs(graph, adj, visited)

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