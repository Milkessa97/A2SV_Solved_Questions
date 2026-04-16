# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def total(root):
            nonlocal max_sum
            if not root:
                return 0
            
            left = max(total(root.left),0)
            right = max(total(root.right),0)

            curr = root.val + left + right
            max_sum = max(max_sum,curr)

            return root.val + max(left,right)
        
        total(root)
        return max_sum
