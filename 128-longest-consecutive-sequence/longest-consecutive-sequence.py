class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        nums.sort()

        for num in nums:
            if num-1 in d:
                d[num] = d[num-1]+1
            else:
                d[num] = 1
                
        if d:
            return max(d.values())
        else:
            return 0