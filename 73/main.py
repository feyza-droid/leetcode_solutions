class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #TODO: Try O(1) space solution
        key = 0
        
        x_indexes = {}
        y_indexes = {}
        
        m = len(matrix)
        n = len(matrix[0])
        
        x = 0
        while(x < m):
            if (x_indexes.get(x) == None):
                y = 0
                while(y < n):
                    if matrix[x][y] == key:
                        x_indexes.update({x: True})
                        if (y_indexes.get(y) == None):
                            y_indexes.update({y: True})    
                    y += 1
            x += 1
                    
        for x in x_indexes.keys():
            for y in range(n):
                matrix[x][y] = key
                
        for y in y_indexes.keys():
            for x in range(m):
                matrix[x][y] = key
