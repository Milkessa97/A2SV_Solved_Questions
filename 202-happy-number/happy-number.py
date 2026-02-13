class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while n != 1:
            if n == 1:
                return True
            if n in check:
                return False
            check.add(n)
            n = sum([pow(int(i),2) for i in str(n)])
        else:
            return True
