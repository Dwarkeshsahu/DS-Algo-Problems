"""
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Example 2:

Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= left <= right <= 109

Solution summary:-

By seeing array we know element which are greater than right limit , will become breaking points.

We can break this problem in 3 parts.
a:- when element is in range. (left<= element <= right)
b:- when element less than left. ( element < left )
c:- when element greater than right. ( right < element)

a: we can direct calculate.
b: we need old count as new element is not in range , so ending at new element(without max element in subarry) won't usefull cases.
max element = 5
left = 2
eg:- 4,5,3,8,1
cases: - 
        1 (not useful when max is 5, because subarray doesn't contain 5 ) 
      2,1 (not useful when max is 5, because subarray doesn't contain 5 )
    3,2,1 (not useful when max is 5, because subarray doesn't contain 5 )
  5,3,2,1 (usefull)
4,5,3,2,1 (usefull)
count = 2 , which will present in previous count.


"""


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        start = 0
        prev_count = 0
        overall_count = 0
        for end in range(len(nums)):
            if nums[end] >= left and nums[end] <= right:
                prev_count = end-start+1
                overall_count += prev_count
            elif nums[end] < left:
                overall_count += prev_count
            else:
                start = end+1
                prev_count = 0
                
        return overall_count
