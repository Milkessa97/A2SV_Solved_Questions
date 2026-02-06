class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while len(s) > 1:
            l = [int(x) for x in s.strip()]
            s = str(sum(l))
        return int(s)