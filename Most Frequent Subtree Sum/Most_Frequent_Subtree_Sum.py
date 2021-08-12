"""
https://leetcode.com/problems/most-frequent-subtree-sum/

Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

Example 1:


Input: root = [5,2,-3]
Output: [2,-3,4]
Example 2:


Input: root = [5,2,-5]
Output: [2]
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

Solution Summary:-
Using map store all sum as key and sum frequency(counts) as value.
Filter keys(subtree sum) with max freq value(count).

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findFrequentTreeSumHelper(self, root):
        if root is None:
            return 0
        
        a = self.findFrequentTreeSumHelper(root.left)
        b = self.findFrequentTreeSumHelper(root.right)
        currSum = a + b + root.val
        if currSum not in self.maxSumMap:
            self.maxSumMap[currSum] = 0
        self.maxSumMap[currSum]+=1
        return currSum
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.maxSumMap = {}
        self.findFrequentTreeSumHelper(root)
        maxFreq = max(self.maxSumMap.values())
        return filter(lambda x : self.maxSumMap[x] == maxFreq, self.maxSumMap)
        
        
