class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = str(num)
            stripped = list(map(int,num.strip()))
            res.extend(stripped) 
        return res
