# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, newRoot):
            def check(root,newRoot):
                if not root and not newRoot:
                    return True
                
                if not root or not newRoot:
                    return False
                
                if root.val != newRoot.val:
                    return False
                
                left = check(root.left, newRoot.left)
                right = check(root.right,newRoot.right)

                return left and right
            
            return check(root,newRoot)

        def dfs(root):
            if not root:
                return False

            if root.val == subRoot.val:
                if isSameTree(root,subRoot):
                    return True
            
            left = dfs(root.left)
            right = dfs(root.right)

            return left or right
        
        return dfs(root)
