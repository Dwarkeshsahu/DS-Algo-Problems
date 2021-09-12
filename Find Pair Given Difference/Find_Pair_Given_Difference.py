"""
https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1#

Given an array Arr[] of size L and a number N, you need to write a program to find if there exists a pair of elements in the array whose difference is N.

Example 1:

Input:
L = 6, N = 78
arr[] = {5, 20, 3, 2, 5, 80}
Output: 1
Explanation: (2, 80) have difference of 78.
Example 2:

Input:
L = 5, N = 45
arr[] = {90, 70, 20, 80, 50}
Output: -1
Explanation: There is no pair with difference of 45.
Your Task:
You need not take input or print anything. Your task is to complete the function findPair() which takes array arr, size of the array L and N as input parameters and returns True if required pair exists, else return False.

Expected Time Complexity: O(L* Log(L)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ L ≤ 104
1 ≤ Arr[i], N ≤ 105


Sol:-
Two sum idea won't work  as in left increment or right decrement BOTH will reduce difference.

Sort array.
So best approach to start from i and j(i+1).
if diff is less then increament j so diff will increase.
if  diff is greater than target , the increament i so it will reduce delta (diff) from i and j.

"""
class Solution:

    def findPair(self, arr, L,N):
        arr.sort()
        i = 0
        j = i+1
        while j < L:
            diff = arr[j] - arr[i]
            if diff == N:
                return True
            elif diff < N:
                j+=1
            else:
                i+=1
            
        return False
