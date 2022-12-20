def dfs(graph, source):
    print(f"node {source}")

    for adj in graph[source]:
        dfs(graph, adj)

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}
dfs(graph, source = 'a') # pick any node as the starting node