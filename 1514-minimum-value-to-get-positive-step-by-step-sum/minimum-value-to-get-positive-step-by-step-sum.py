class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pref = 0
        min_pref = 0

        for num in nums:
            pref += num
            min_pref = min(min_pref, pref)

        return 1 - min_pref