"""
https://leetcode.com/problems/partition-array-into-disjoint-intervals/



simple solution using left max prefix array and right min postfix array:
then whereever they do not cross is the answer
this can be done in single loop if we can maintain max value seen so far variable
and left max valiable
"""

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftmax = nums[0]
        maxInRun = nums[0]
        ans = 0
        for i in range(1,len(nums)):
            if nums[i] > maxInRun:
                maxInRun = nums[i]
            elif nums[i] < leftmax:
                ans = i
                leftmax = maxInRun
        return ans+1
        
