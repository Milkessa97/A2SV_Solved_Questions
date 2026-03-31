class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        posA = bisect_left(nums,target)
        posB = bisect_right(nums,target)
        if posA < len(nums) and nums[posA] == target:
            return [posA,posB-1]
        else:
            return [-1,-1]