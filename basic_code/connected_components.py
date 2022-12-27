def count_connected_components(graph):
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited) # starting node
            # print(f"End of a connected component")
            count += 1

    return count



def dfs(graph, source, visited):    
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

count = count_connected_components(graph)
print(f"count {count}")