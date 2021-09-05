"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


Solution summary:-
#Solution 1
left = 0 and right = n-1
calculate square of both side and add max squre to result in reverse order and update left or right( whose suare is max)


#solution 2
# find break point(negative to positive) and then move left and right and add into result

"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left , right = 0, len(nums)-1
        squareArray = [None for i in range(right+1)]
        insertIndex = right
        
        while left <= right:
            leftSQuare = nums[left]*nums[left]
            rightSQuare = nums[right]*nums[right]
            if leftSQuare < rightSQuare:
                squareArray[insertIndex] = rightSQuare
                right-=1
            else:
                squareArray[insertIndex] = leftSQuare
                left+=1
            insertIndex-=1
        return squareArray
                
        


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n =  len(nums)
        i = 0
        
        while i < n and nums[i] < 0:
            i+=1
        j = i
        i-=1
        
        result = []
        while i >= 0 and j < n:
            if abs(nums[i])  < nums[j]:
                result.append(nums[i]**2)
                i-=1
            else:
                result.append(nums[j]**2)
                j+=1
        while i >= 0:
            result.append(nums[i]**2)
            i-=1
        while j < n:
            result.append(nums[j]**2)
            j+=1
        return result
            
