class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Updating the indeces of my num to negative number, 
        and if I found out that the number is already negative, 
        that means the index was already accessed"""
        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            else:
                nums[abs(num) - 1] = -nums[abs(num) - 1]