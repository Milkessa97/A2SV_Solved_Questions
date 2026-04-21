class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        low, high = 0, max(houses[-1], heaters[-1])

        while low <= high:
            mid = (low + high) // 2
            
            idx = 0
            for heater in heaters:
                left = heater - mid
                right = heater + mid

                while idx < len(houses) and left <= houses[idx] <= right:
                    idx += 1
                
                if idx == len(houses):
                    high = mid - 1
                    break
            else:
                low = mid + 1
            
        return low