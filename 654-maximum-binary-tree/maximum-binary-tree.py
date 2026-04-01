# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recurse(nums):
            if not nums:
                return
            max_idx = 0
            for idx in range(len(nums)):
                if nums[idx] > nums[max_idx]:
                    max_idx = idx

            curr_root = TreeNode()
            curr_root.val = nums[max_idx]
            curr_root.left = recurse(nums[:max_idx])
            curr_root.right = recurse(nums[max_idx+1:])

            return curr_root
        
        return recurse(nums)
