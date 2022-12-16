# 48. Rotate Image
class Solution:        
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1 # nxn matrix so #rows = #columns
        t, b = 0, len(matrix)-1


        while(l < r):
            for i in range(r - l): # from left to right-1
                t, b = l, r # square matrix

                # save the top left
                temp = matrix[t][l + i]
                
                # move bottom left into top left
                matrix[t][l + i] = matrix[b - i][l]

                # move bottom right into bottom left
                matrix[b - i][l] = matrix[b][r - i]

                # move top right into bottom right
                matrix[b][r - i] = matrix[t + i][r]

                # move top left into top right
                matrix[t + i][r] = temp

            l += 1
            r -= 1