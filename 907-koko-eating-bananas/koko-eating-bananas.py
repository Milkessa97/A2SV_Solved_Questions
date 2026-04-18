class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            curr = 0

            for pile in piles:
                curr += ceil(pile / mid)
                if curr > h:
                    break

            if curr > h:
                left = mid + 1
            else:
                right = mid - 1

        return left
