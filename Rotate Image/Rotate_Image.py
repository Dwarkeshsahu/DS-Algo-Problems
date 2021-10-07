"""
https://leetcode.com/problems/rotate-image/

rotate through diagonal and then columns wise swapping
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for dig in range(n):
            row = dig
            for col in range(dig+1, n):
                matrix[row][col] , matrix[col][row] =  matrix[col][row], matrix[row][col]
        print(matrix)
        left = 0
        right = n-1
        while left < right:
            for row in range(n):
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
            left+=1
            right-=1
        
        
