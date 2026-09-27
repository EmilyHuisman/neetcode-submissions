# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
        
        
        '''
        #09/27
        # swap every child breadth first
        def swap(self, node):
            tempRight = node.right
            node.right = node.left
            node.left = tempRight
        
        
        cur = root
        
        if not cur:
            return root
        
        queue = [cur]
        
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            swap(self, current)
        return root
        '''








