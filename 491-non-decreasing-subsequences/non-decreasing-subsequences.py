class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(idx):
            nonlocal res, curr

            if idx == len(nums):
                if len(curr) > 1:
                    if curr not in res:
                        res.append(curr.copy())
                return
            
            if not curr:
                curr.append(nums[idx])
                backtrack(idx+1)
                curr.pop()
                backtrack(idx+1)
            else:
                if nums[idx] >= curr[-1]:
                    curr.append(nums[idx])
                    backtrack(idx+1)
                    curr.pop()
                backtrack(idx+1)
            
        backtrack(0)
        return res