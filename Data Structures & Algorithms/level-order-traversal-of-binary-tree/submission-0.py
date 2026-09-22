# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        sublist = []
        
        queue = deque()

        if root:
            queue.append(root)
        
        while len(queue) > 0:

            for i in range(len(queue)):
                curr = queue.popleft()
                sublist.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(sublist)
            sublist = []
        return ans