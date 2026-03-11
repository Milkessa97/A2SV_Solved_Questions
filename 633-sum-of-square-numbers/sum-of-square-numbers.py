class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(sqrt(c))
        while a <= b:
            a_sqr = pow(a,2)
            b_sqr = pow(b,2)
            if a_sqr + b_sqr == c:
                return True
            elif a_sqr + b_sqr < c:
                a += 1
            else:
                b -= 1
        return False
