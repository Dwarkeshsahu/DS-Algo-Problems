"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


Solution Summary:-
Basic concept is search two times lower bound of target in array.
first time search for target lower bound in array.
second time search for target+1 lower bound in array and then reduce 1 from index to get upper bound target.
Or we can do directly with upper bound.

Both implmentation are here.
one with bisect module , which give upper bound function as bisect.bisect_left(array, target).
other is binary implementation , with first find postion saved in every array[mid] == target condition.
"""


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left = 0
#         right = len(nums)-1
#         firstIdx = endIdx = -1
#         while left <= right:
#             mid = left + (right-left)//2
#             if nums[mid] == target:
#                 firstIdx = mid
#                 right =  mid-1
#             elif nums[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid -1
                
#         left = 0
#         right = len(nums)-1
#         while left <= right:
#             mid = left + (right-left)//2
#             if nums[mid] == target:
#                 endIdx = mid
#                 left =  mid+1
#             elif nums[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid -1
#         return [firstIdx , endIdx]
        

# import bisect    
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         first = second = -1
#         first = bisect.bisect_left(nums, target)
#         second = bisect.bisect_left(nums, target+1)-1
#         if first <= second:
#             return [first, second]
#         return [-1, -1]
        
        
class Solution:
    
    
    def getLowerBound(self, nums: List[int], target: int):
        left = 0
        right = len(nums)-1
        first_pos = right+1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                first_pos = mid
                right = mid-1
            else:
                left = mid+1
        return first_pos
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.getLowerBound(nums, target)
        second = self.getLowerBound(nums, target+1)-1
        if first <= second:
            return [first,second]
        return [-1,-1]
        
        
        
        
        
        
