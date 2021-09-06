"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109



Solution Summary:-
there will be atmost 2  element which can have freq greater then n/3.

So making triplets 

Else -> Else part is for making triplets.
Othere wise count increase and update val1 , val2 if count becomes 0
Count the frequency to be sure about val1 and val2 are having greater than n/3 frequency.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val1 = nums[0]
        val2 = nums[0]
        count1 = 0
        count2  = 0

        for num in nums:
            if num == val1:
                count1 = count1 + 1
            elif num == val2:
                count2 = count2 + 1
            else:
                if count1 == 0:
                    val1 = num
                    count1 = 1
                elif count2 == 0:
                    val2 = num
                    count2 = 1
                else:
                    count1 = count1 -1
                    count2 = count2 -1
                    
        count1 = count2 = 0        
        for num in nums:
            if val1 == num:
                count1+=1
            if val2 == num:
                count2 +=1
            
        result = []
        if count1 > len(nums)//3:
            result.append(val1)
        if val1 != val2 and count2 > len(nums)//3:
            result.append(val2)
        return result
