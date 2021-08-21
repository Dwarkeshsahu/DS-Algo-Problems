"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

Solution summary:-'
(second solution)
Put First k element in heap.
now from next element onwords from list , we will check whether this new element is smaller or greater from top of min Heap.
if it is greater then min heap top , then pop heap and push this element.
at the end top element will heave kth largest element in min heap. 




"""

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums = [-num for num in nums]
#         heapq.heapify(nums)
#         while k-1:
#             heapq.heappop(nums)
#             k-=1
#         return -heapq.heappop(nums)
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
        return heap[0]
