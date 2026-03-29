# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        check = defaultdict(int)
        check[0] = 1

        def path(root,curr_sum):
            nonlocal count
            if not root:
                return
            
            curr_sum += root.val
            
            count += check[curr_sum - targetSum]
            check[curr_sum] += 1

            path(root.left,curr_sum)
            path(root.right,curr_sum)

            check[curr_sum] -= 1
        
        path(root,0)
        return count
