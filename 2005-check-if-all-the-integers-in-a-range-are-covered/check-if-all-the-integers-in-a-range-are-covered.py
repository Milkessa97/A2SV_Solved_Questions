class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        while left <= right:
            for range in ranges:
                if left >= range[0] and left <= range[1]:
                    break
            else:
                return False
            left += 1
        return True