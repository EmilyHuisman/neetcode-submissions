# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        Given: binary tree
        Goal: return # of good nodes

        Good Node:
            - all values on its path from root are less than its value
        '''
        def preorder(node, maxVal):
            if not node:
                return 0
            if maxVal <= node.val:
                count = 1
            else:
                count = 0
            maxVal = max(node.val, maxVal)
            
            return count + preorder(node.left, maxVal) + preorder(node.right, maxVal)
        return preorder(root, float("-inf"))

        
        