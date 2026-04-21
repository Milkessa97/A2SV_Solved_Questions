class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def solve(x,n):
            if n == 0:
                return 1    

            half = solve(x,n//2)

            if n % 2 == 1:
                return half*half*x
            else:
                return half*half

        pos_exp = solve(x,abs(n))

        if n > 0:
            return pos_exp
        else:
            return 1/pos_exp

