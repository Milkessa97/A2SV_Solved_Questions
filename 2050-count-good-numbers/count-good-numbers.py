class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(base, exp, mod):
            if exp == 0:
                return 1
            if exp == 1:
                return base
            cur = power(base, exp//2, mod)
            cur **= 2
            if exp % 2 == 1:
                cur *= base
            return cur % mod
        evens = ceil(n/2)
        odds = n//2
        mod = pow(10, 9) +7
        return (power(5,evens, mod)*power(4,odds, mod))%mod