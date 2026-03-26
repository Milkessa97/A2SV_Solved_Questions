class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0]*k
        fairness = float('inf')

        def backtrack(idx,curr_max=0):
            nonlocal fairness
            nonlocal child

            if curr_max >= fairness:
                return

            if idx == len(cookies):
                fairness = min(fairness,curr_max)
                return

            for i in range(k):
                child[i] += cookies[idx]
                backtrack(idx+1,max(curr_max,child[i]))
                child[i] -= cookies[idx]

                if child[i] == 0:
                    return

        backtrack(0)
        return fairness

        