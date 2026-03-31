class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low = 1
        high = x

        while low <= high:
            md = (low + high) // 2
            check = md * md

            if check == x:
                return md
            elif check > x:
                high = md - 1
            else:
                low = md + 1

        return high