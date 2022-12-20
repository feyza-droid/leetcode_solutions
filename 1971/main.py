# 1971. Find if Path Exists in Graph
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
            
        is_visited = [False for _ in range(n)]

        graph = {}
        for edge_pair in edges:
            edge1, edge2 = edge_pair

            if edge1 not in graph:
                graph[edge1] = [edge2]
            else:
                graph[edge1].append(edge2)

            if edge2 not in graph:
                graph[edge2] = [edge1]
            else:
                graph[edge2].append(edge1)

        return self.path_rec(graph, is_visited, source, destination)

    def path_rec(self, graph, is_visited, source, destination):
        is_visited[source] = True
        adj_list = graph[source]
        if destination in adj_list:
            return True
        
        is_path = False
        for adj in adj_list:
            if not is_visited[adj]:
                is_path = self.path_rec(graph, is_visited, adj, destination)
                if is_path:
                    return True

        return is_path 