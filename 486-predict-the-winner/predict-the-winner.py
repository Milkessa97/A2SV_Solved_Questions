class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recurse(left,right):
            if left == right:
                return nums[right]
            
            pick_left = nums[left] - recurse(left + 1, right)
            pick_right = nums[right] - recurse(left, right - 1)
            
            return max(pick_left, pick_right)
    
        return recurse(0, len(nums) - 1) >= 0