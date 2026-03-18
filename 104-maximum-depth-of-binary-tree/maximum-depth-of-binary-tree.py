# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(root,depth=0):
            nonlocal max_depth
            if not root:
                return

            depth += 1
            dfs(root.left,depth)
            dfs(root.right,depth)

            max_depth = max(max_depth,depth)
            depth -= 1

        dfs(root)
        return max_depth
