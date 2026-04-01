class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        check = []
        def backtrack(i=0,curr = []):
            nonlocal res,check
            if i == len(nums):
                if Counter(curr) not in check:
                    res.append(curr.copy())
                    check.append(Counter(curr))
                return

            curr.append(nums[i])
            backtrack(i+1,curr)
            curr.pop()
            backtrack(i+1,curr)

        backtrack()
        return res