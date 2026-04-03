class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        visited_idx = set()
        def permutate():
            nonlocal curr,ans
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if i not in visited_idx:
                    curr.append(nums[i])
                    visited_idx.add(i)
                    permutate()
                    curr.pop()
                    visited_idx.remove(i)
        
        permutate()
        return ans
