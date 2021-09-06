"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

Solution summary:-
use moore's vating algorithm 
make pair oof two different elements,
last value which is remaing in val will be greater than n/2 freq.


if surity is not given that majority element will be always present then we have to loop for counting val frequnecy and if gtreater than n/2 otherewise no element.

for more detail
https://www.youtube.com/watch?v=PUCEWmefFm4


"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = nums[0]
        for i in range(len(nums)):
            if val == nums[i]:
                count+=1
            else:
                if count > 0:
                    count-=1
                else:
                    val = nums[i]
                    count = 1
        return val
