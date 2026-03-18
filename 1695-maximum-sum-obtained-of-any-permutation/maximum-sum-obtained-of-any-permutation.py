class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        queries = [0]*(len(nums)+1)
        for req in requests:
            queries[req[0]] += 1
            queries[req[1]+1] -= 1
        pref=[]
        for quer in queries:
            if not pref:
                pref.append(quer)
            else:
                pref.append(pref[-1]+quer)
        pref = pref[:len(nums)]
        pref.sort()
        nums.sort()
        res = 0
        mod = 10**9 + 7

        for i in range(len(nums)):
            res += nums[i] * pref[i]

        return res % mod