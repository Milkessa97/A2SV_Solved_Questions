class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(i=1,arr=[]):
            if len(arr) == k:
                ans.append(arr.copy())
                return

            if i>n:
                return

            arr.append(i)
            backtrack(i+1,arr)
            
            arr.pop()
            backtrack(i+1,arr)

        backtrack()
        return ans

