class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        p = 0
        while p < len(s1):
            if s1[p] == 'x' and s2[p] == 'y':
                xy += 1
            elif s1[p] == 'y' and s2[p] == 'x':
                yx += 1
            p += 1

        if (xy + yx) % 2 == 1:
            return -1
        
        res = xy // 2 + yx // 2

        if xy % 2:
            return res + 2
        else:
            return res