"""

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109


Sol:-
same as two sum three sum with extra loop for fourth value
O(N^3) Time
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        twosum = []
        while left < right:
            if left > 0 and numbers[left] == numbers[left-1]:
                left+=1
                continue
            summ = numbers[left] + numbers[right]
            if summ == target:
                twosum.append([numbers[left] , numbers[right]])
                left+=1
                right-=1
            elif summ < target:
                left+=1
            else:
                right-=1
        return twosum
    
    def threeSum(self, nums: List[int], target, n) -> List[List[int]]:
        result = []
        for i in range(n):
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            twosum = self.twoSum(nums[i+1:], target-nums[i])
            for tup in twosum:
                tup += [nums[i]]
                result.append(tup)
        return result
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        
        for i in range(n-2):
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            threeSum = self.threeSum(nums[i+1:], target-nums[i], n-i-1)
            for tup in threeSum:
                tup += [nums[i]]
                result.append(tup)
        return result
    
    
    
