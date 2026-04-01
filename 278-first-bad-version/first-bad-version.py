# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left+right) // 2
            if isBadVersion(mid):
                if mid == 1:
                    return 1
                if isBadVersion(mid-1):
                    right = mid - 1
                else:
                    return mid
            else:
                left = mid + 1