class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def powerSet(idx,curr=[]):
            nonlocal ans
            
            if idx == len(nums):
                ans.append(curr.copy())
                return
            powerSet(idx+1,curr+[nums[idx]])
            powerSet(idx+1,curr)

        powerSet(0,[])
        return ans
