"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1



approach 2 :

add element in set and check from 1 to len(nums)
Think on why we need to check only till length of array

approach 1 :
step 1: make elements in range between 1 to n(length)
step 2: mark negative,  index of array its presence with the help of index value.
step 3: find positive if present and return i+1 else n+1

"""
Time O(N), Space O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        one = False
        # make in range
        for i in range(n):
            if nums[i] == 1:
                one = True
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 1
        if one is False:
            return 1
        
        # mark 
        for i in range(n):
            val = abs(nums[i]) -1
            nums[val] = -abs(nums[val])
    
        # find 
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1
        
        
Time O(N), Space O(N)
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n = len(nums)
#         hashset = set(nums)

#         for i in range(1,n+1):
#             if i not in hashset:
#                 return i
#         return n+1
            
        

        
