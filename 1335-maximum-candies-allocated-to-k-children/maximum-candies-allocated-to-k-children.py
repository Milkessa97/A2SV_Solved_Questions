class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low, high = 1,max(candies)

        while low <= high:
            mid = (low + high) // 2
            childs = 0
            for pile in candies:
                childs += pile // mid

            if childs >= k:
                low = mid + 1
            else:
                high = mid - 1

        return low - 1