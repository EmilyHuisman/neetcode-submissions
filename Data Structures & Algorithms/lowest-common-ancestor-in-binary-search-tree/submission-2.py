# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur
        




        '''
        # 09/27
        if p.left is q or p.right is q:
            return p
        elif q.left is p or q.right is p:
            return q
        else:
            while (root.val > p.val and root.val > q.val) or (root.val < p.val and root.val < q.val):
                if root.val > p.val:
                    root = root.left
                else:
                    root = root.right
            
        return root
        '''