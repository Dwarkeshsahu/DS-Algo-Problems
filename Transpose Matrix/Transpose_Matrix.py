"""
https://leetcode.com/problems/transpose-matrix/

"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        matrix_trans = [[None for i in range(n)] for j in range(m)]
        
        for row in range(n):
            for col in range(m):
                matrix_trans[col][row] = matrix[row][col] 
        return matrix_trans
                                            
