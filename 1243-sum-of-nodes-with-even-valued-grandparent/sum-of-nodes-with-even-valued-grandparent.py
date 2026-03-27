# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        stack = []
        res = 0

        def search(root):
            nonlocal stack
            nonlocal res
            if root:
                if len(stack) > 1 and stack[-2] % 2 == 0:
                    res += root.val

                stack.append(root.val)
                search(root.left)
                search(root.right)
                stack.pop()

        search(root)
        return res
