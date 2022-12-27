def largest_connected_component(graph):
    visited = set()
    max_count = 0
    for node in graph:
        if node not in visited:
            number_of_nodes = dfs(graph, node, visited) # starting node
            max_count = max(max_count, number_of_nodes)
            # print(f"End of a connected component with number_of_nodes {number_of_nodes}")

    return max_count



def dfs(graph, source, visited, number_of_nodes = 0):    
    visited.add(source)
    number_of_nodes += 1
    # print(f"source {source} number_of_nodes {number_of_nodes}")

    for adj in graph[source]:
        if adj not in visited:
            number_of_nodes = dfs(graph, adj, visited, number_of_nodes)
    
    return number_of_nodes

graph = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

count = largest_connected_component(graph)
print(f"largest_connected_component has {count} nodes")