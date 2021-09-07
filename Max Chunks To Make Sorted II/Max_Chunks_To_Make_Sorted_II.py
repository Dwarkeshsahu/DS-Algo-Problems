"""
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

 

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
 

Constraints:

1 <= arr.length <= 2000
0 <= arr[i] <= 108



find max of  left and min  of right and see relation

"""

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        right_min = float("inf")
        minArr = [None for _ in range(n)]
        for i in reversed(range(n)):
            right_min = min(arr[i], right_min)
            minArr[i] = right_min
        
        left_max = float("-inf")
        chunks = 1
        for i in range(n-1):
            left_max = max(arr[i], left_max)
            if left_max <= minArr[i+1]:
                chunks+=1
        return chunks
            
