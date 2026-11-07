# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''

        L N R
        '''
        ans = 0
        count = 0
        def inorder(node):
            nonlocal ans
            if not node:
                return 0
            
            left = inorder(node.left)
            
            right = inorder(node.right)
            ans = max(ans, left+right)
            return 1 + max(left, right)
        
        inorder(root)
        return ans