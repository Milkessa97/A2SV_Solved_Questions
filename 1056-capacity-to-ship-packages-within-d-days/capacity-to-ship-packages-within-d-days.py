class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        while low <= high:
            mid = (low + high) // 2

            count_day = 0
            curr_weight = 0
            prev_weight = 0
            for weight in weights:
                curr_weight += weight

                if curr_weight > mid:
                    count_day += 1
                    curr_weight -= prev_weight
                
                prev_weight = curr_weight
            
            if count_day < days:
                high = mid - 1
            else:
                low = mid + 1
        return low
