class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        NOTE:
        According to Python wiki: Time complexity, set is implemented as a hash table. So you can expect to lookup/insert/delete in O(1) average. 
        Unless your hash table's load factor is too high, then you face collisions and O(n).
        """
        
        """
        Time Complexity = O(mn)
        Space Complexity = O(max(m,n)) 
        """

        """
        TODO: 
        Try O(1) space solution
        """
        
        KEY = 0
        rows = set()
        cols = set()
        m = len(matrix)
        n = len(matrix[0])
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == KEY:
                    rows.add(r) # O(1)
                    cols.add(c) # O(1)
                    
        for r in rows:
            for c in range(n):
                matrix[r][c] = KEY
                
        for c in cols:
            for r in range(m):
                matrix[r][c] = KEY