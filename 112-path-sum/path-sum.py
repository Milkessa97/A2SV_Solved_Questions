# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:      
        def calculate(node,curr = 0):
            if not node:
                return False
            
            curr += node.val

            if not node.left and not node.right:
                if curr == targetSum:
                    return True
                return False

            left = calculate(node.left,curr)
            right = calculate(node.right,curr)
            
            return left or right
        return calculate(root)