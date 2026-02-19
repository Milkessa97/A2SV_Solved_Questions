class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        if len(nums) == 1:
            return str(nums[0])

        for i in range(len(nums)-1):
            for j in range(len(nums)-1,i,-1):
                if nums[j]+nums[j-1] > nums[j-1]+nums[j]:
                    nums[j],nums[j-1]=nums[j-1],nums[j]

        if nums[0] == '0':
            return '0'

        return ''.join(nums)