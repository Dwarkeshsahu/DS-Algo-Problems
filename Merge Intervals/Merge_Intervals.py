"""
https://leetcode.com/problems/merge-intervals/
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            start , end = intervals[i][0], intervals[i][1]
            if result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start,end])
        return result
                
