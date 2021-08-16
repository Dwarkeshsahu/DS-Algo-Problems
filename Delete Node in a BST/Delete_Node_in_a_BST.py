"""
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Follow up: Can you solve it with time complexity O(height of tree)?

 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMax(self,node):
        if node.right is None:
            return node
        
        return self.findMax(node.right)
        
    
    
    def deleteNodeHelper(self, node, key):
        
        if node is None:
            return node
        
        if node.val == key:
            if node.left is None and node.right is None:
                return None
            elif node.left is None or node.right is None:
                if node.left is not None:
                    return node.left
                return node.right
            else:
                maxNode = self.findMax(node.left)
                node.left = self.deleteNodeHelper(node.left, maxNode.val)
                node.val = maxNode.val
                return node
                

        elif node.val > key:
            node.left = self.deleteNodeHelper(node.left, key)
        else:
            node.right = self.deleteNodeHelper(node.right, key)
            
        return node
        
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.deleteNodeHelper(root, key)
        
