"""
https://www.lintcode.com/problem/912/


Description
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example
Example 1:

Input:
[[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output:
6

Explanation:
The point `(0,2)` is an ideal meeting point, as the total travel distance of `2 + 2 + 2 = 6` is minimal. So return `6`.
Example 2:

Input:
[[1,1,0,0,1],[1,0,1,0,0],[0,0,1,0,1]]
Output:
14


Given (Xi, Yi)
X = Sort all Xi
Y = Sort all Yi
find median of both X and Y
so meating point will be 
point_x = Median(X)
point_y = Median(Y)

"""

class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def minTotalDistance(self, grid):
        # Write your code here
        max_row = len(grid)
        max_col = len(grid[0])
        x = []
        y = []
        for row in range(max_row):
            for col in range(max_col):
                if grid[row][col] == 1:
                    x.append(row)
        for col in range(max_col):
            for row in range(max_row):
                if grid[row][col] == 1:
                    y.append(col)
        
        px = x[len(x)//2]
        py = y[len(y)//2]
        min_distance = 0
        for col in range(max_col):
            for row in range(max_row):
                if grid[row][col] == 1:
                    min_distance += abs(row-px) + abs(col-py)

        #                     currDistance += abs(row-pRow) + abs(col-pCol)
        #         min_distance = min(currDistance, min_distance)
        return min_distance








        # min_distance = float("inf")
        # max_row = len(grid)
        # max_col = len(grid[0])
        # for pRow in range(max_row):
        #     for pCol in range(max_col):
        #         currDistance = 0
        #         for row in range(max_row):
        #             for col in range(max_col):
        #                 if grid[row][col] == 1:
        #                     currDistance += abs(row-pRow) + abs(col-pCol)
        #         min_distance = min(currDistance, min_distance)
        # return min_distance


