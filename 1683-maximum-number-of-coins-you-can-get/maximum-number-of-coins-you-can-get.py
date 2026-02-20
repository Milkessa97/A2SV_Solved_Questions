class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = 0
        piles.sort()
        left, right = 0, len(piles)-1

        while left < right - 1:
            triplet = sorted([piles[left], piles[right], piles[right-1]])
            count += triplet[1]
            right -= 2
            left += 1

        return count