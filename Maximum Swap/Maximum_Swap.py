"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108


Solution:-
suffix max array from right to left so we can get right side max value at any time.
Loop from left to right and find smaller number to its right side and swap , will generate max number
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [x for x in str(num)]
        n = len(num)
        suffix_max = [None for _ in range(n)]
        suffix_max[-1] =  n-1
        for i in reversed(range(n-1)):
            if num[suffix_max[i+1]] >= num[i]:
                suffix_max[i] = suffix_max[i+1]
            else:
                suffix_max[i] = i
        for i in range(n):
            if num[i] < num[suffix_max[i]]:
                num[i], num[suffix_max[i]] = num[suffix_max[i]], num[i]
                break
        return int(''.join(num))
            
