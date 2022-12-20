# 1791. Find Center of Star Graph
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node1, node2 = edges[0]
        node3, node4 = edges[1]

        if node1 == node3:
            return node1

        if node1 == node4:
            return node1

        if node2 == node3:
            return node2

        if node2 == node4:
            return node2