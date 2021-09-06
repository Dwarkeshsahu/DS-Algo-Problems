"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1



Solution summary:-
12345 lowest number
54321 biggest numbr by same digit
from right to left , find num[i] < num[i+1]
found break point L.
start from right and find next greter element (ceil element) of break point number(num[L])
swap L and Ceil element and reverse number from L till end.

"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = [x for x in str(n)]
        length = len(num)
        i = length-1
        while i > 0 and int(num[i-1]) >= int(num[i]):
            i-=1
        if i == 0:
            return -1
        L = i-1
        for i in reversed(range(length)):
            if num[i] > num[L]:
                num[i] , num[L] = num[L] , num[i]
                num[L+1:] = num[L+1:][::-1]
                n = int(''.join(num))
                return n if  n<= 2**31-1 else -1
        return -1
        
        
        
                
