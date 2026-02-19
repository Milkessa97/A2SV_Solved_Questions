class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        srt = sorted(nums) 
        res = [0]*len(nums)
        for num in range(len(nums)):
            res[num] = srt.index(nums[num])
        return res