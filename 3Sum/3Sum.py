"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Sol:-
Same as using Two sum with extra loop for third value

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
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        target = 0
        for i in range(n):
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            twosum = self.twoSum(nums[i+1:], target-nums[i])
            for tup in twosum:
                tup += [nums[i]]
                result.append(tup)
        return result
