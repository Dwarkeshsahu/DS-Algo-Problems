"""
https://leetcode.com/problems/range-sum-of-bst/

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

Solution Summary:-

There are three methods which uses almost same Time O(N) and Space O(N) complexities.
Method 1:
Travel from each node {O(N) Time} and search k-node.val in tree {O(h) h is height , where O(logN) in best case and O(N) in worst case}. 

Method 2:
Use Set or HashMap for storing k-node.val and then evrytime check if compliment is present in set or map.
O(N) Time for tree traversal and O(N) space for storing node values.

Method 3:
Use Inorder Traversal (which will give sorted list in BST) and create a list and Use two pointer search on this sorted list.
O(N) Time and O(N) space for array list.



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findPair(self,node,k):
        
        if not node:
            return False
        if node.val == k:
            return True
        
        elif node.val > k:
            ans = self.findPair(node.left,k)
        else:
            ans = self.findPair(node.right,k)
        return ans    
    
    def findTargetHelper(self, node: Optional[TreeNode], k: int, root):
        
        if not node:
            return False
        
        ans = False
        compliment = k-node.val
        if compliment > node.val:
            ans = self.findPair(root,compliment)
        if ans is True:
            return True
        
        return self.findTargetHelper(node.left,k,root) or self.findTargetHelper(node.right,k,root)
        
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.findTargetHelper(root, k, root)


