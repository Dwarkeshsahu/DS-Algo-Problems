"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000


Solution:-
1. Find root to target node path
2. This path will be used in finding k distance while reducing k once we go upside(root side)
3. There will be a blacklist node for every node , from where we are coming form target side.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def getRootToNodePath(self,node,target, path):
        
        if node is None:
            return
        
        if node == target:
            self.targetPath = path + [node]
            return
        
        self.getRootToNodePath(node.left,target, path + [node])
        self.getRootToNodePath(node.right,target, path+[node])
        
    
    def getKLevelDownNode(self, node, k, blockedNode):
        
        if node is None or node == blockedNode or k < 0:
            return         
        if k == 0:           
            self.downwordNodes.append(node.val)
            return 
        
        self.getKLevelDownNode(node.left, k-1, blockedNode)
        self.getKLevelDownNode(node.right, k-1, blockedNode)
        
        
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.targetPath = []
        self.downwordNodes = []
        self.getRootToNodePath(root,target, [])
        rootToTargetPath = self.targetPath[::-1]
        
        for i,node in enumerate(rootToTargetPath):
            blockedNode = None if i==0 else rootToTargetPath[i-1]
            self.getKLevelDownNode(rootToTargetPath[i], k-i, blockedNode)
        
        return self.downwordNodes
        
        
