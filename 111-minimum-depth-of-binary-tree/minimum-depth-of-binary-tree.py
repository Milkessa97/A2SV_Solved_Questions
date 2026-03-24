# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        min_depth = float('inf')

        def dfs(root,depth=0):
            nonlocal min_depth

            if not root:
                return

            if not root.left and not root.right:
                min_depth = min(min_depth,depth+1)
                return

            dfs(root.left,depth+1)
            dfs(root.right,depth+1)

        dfs(root)
        return min_depth