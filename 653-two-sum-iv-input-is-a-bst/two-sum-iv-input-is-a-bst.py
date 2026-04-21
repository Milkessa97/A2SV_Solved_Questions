# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inOrder = []

        def traverse(node):
            nonlocal inOrder
            if not node:
                return
            
            traverse(node.left)
            inOrder.append(node.val)
            if inOrder and inOrder[0] + node.val > k:
                return
            traverse(node.right)
        
        traverse(root)
        left,right = 0,len(inOrder)-1

        while left < right:
            if inOrder[left] + inOrder[right] > k:
                right -= 1
            elif inOrder[left] + inOrder[right] < k:
                left += 1
            else:
                return True
        return False
