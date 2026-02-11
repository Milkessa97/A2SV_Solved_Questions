
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_diff = defaultdict(int) 

        for index in range(len(nums)):
            if nums[index] in map_diff:
                return [map_diff[nums[index]], index]
                
            map_diff[target - nums[index]] = index