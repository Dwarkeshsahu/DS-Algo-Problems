"""
https://www.geeksforgeeks.org/count-1s-sorted-binary-array/

Given a binary array sorted in non-increasing order, count the number of 1’s in it. 

Examples: 

Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
Output: 2

Input: arr[] = {1, 1, 1, 1, 1, 1, 1}
Output: 7

Input: arr[] = {0, 0, 0, 0, 0, 0, 0}
Output: 0

"""

# Code 1
class Solution:
    def countOnes(self,arr, N):
        left = 0
        right = N-1
        while left<= right:
            mid = (left+right)//2
            if arr[mid] == 0:
                right = mid-1
            else:
                if mid == right or arr[mid+1] == 0:
                    return mid+1
                else:
                    left = mid+1
        return 0
        

#  code with improvement for early stopping

class Solution:
    def countOnes(self,arr, N):
        left = 0
        right = N-1
        while left<= right:
            mid = (left+right)//2
            
            if arr[mid] == 0:
                if left == mid or arr[mid-1] == 1:
                    return mid
                else:
                    right = mid-1
            else:
                if mid == right or arr[mid+1] == 0:
                    return mid+1
                else:
                    left = mid+1
        return 0
            
