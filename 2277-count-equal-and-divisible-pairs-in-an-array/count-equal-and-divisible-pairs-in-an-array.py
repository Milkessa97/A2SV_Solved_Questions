class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for num1 in range(len(nums)):
            for num2 in range(num1 + 1,len(nums)):
                if nums[num1] == nums[num2] and num1*num2 % k == 0:
                    count+=1
        return count