class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        cost = 0

        for inst in instructions:
            entry = bisect_left(nums,inst)
            end = bisect_right(nums,inst)

            cost += min(entry, len(nums) - end)
            nums.insert(entry,inst)
        
        return cost % (10**9 + 7)