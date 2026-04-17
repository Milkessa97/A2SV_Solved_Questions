# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return True, 0, float('inf'), float('-inf')
            
            left_BST, left_sum, left_min, left_max = dfs(node.left)
            right_BST, right_sum, right_min, right_max = dfs(node.right)

            if left_BST and right_BST and left_max < node.val < right_min:
                res = max(res, node.val + left_sum + right_sum)
                return True, left_sum + right_sum + node.val, min(node.val, left_min), max(node.val,right_max)

            return False, 0, 0, 0
        
        dfs(root)
        return res
            