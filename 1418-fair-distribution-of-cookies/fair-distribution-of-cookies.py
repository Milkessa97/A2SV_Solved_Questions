class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0]*k
        fairness = float('inf')

        def backtrack(idx,_max=0):
            nonlocal fairness
            nonlocal child
            if _max >= fairness:
                return

            if idx == len(cookies):
                fairness = min(fairness,_max)
                return

            for i in range(k):
                child[i] += cookies[idx]
                backtrack(idx+1,max(_max,child[i]))
                child[i] -= cookies[idx]

        backtrack(0)
        return fairness

        