"""

https://www.lintcode.com/problem/903/

Description
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example
Given:
length = 5,
updates = 
[
[1,  3,  2],
[2,  4,  3],
[0,  2, -2]
]
return [-2, 0, 3, 5, 3]

Explanation:
Initial state:
[ 0, 0, 0, 0, 0 ]
After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]
After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]
After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]

Sol:-
Use prefix sum technique for all query only for start index update with increament.


"""

class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        result = [0 for _ in range(length)]
        
        for start, end, inc in updates:
            result[start] += inc
            if end < length-1:
                result[end+1] -= inc

        for i in range(1,length):
            result[i] = result[i-1]+ result[i]

        return result

