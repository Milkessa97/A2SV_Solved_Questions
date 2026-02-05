class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        idx = 0
        while left <= right:
            for rng in range(idx,len(ranges)):
                if left >= ranges[rng][0] and left <= ranges[rng][1]:
                    idx = rng
                    break
            else:
                return False
            left += 1
        return True