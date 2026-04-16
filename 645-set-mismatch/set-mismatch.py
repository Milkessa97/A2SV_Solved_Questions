class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = [0,0]
        check = 1
        for key in count.keys():
            if count[key] == 2:
                res[0] = key
            if not count[check]:
                res[1] = check
            check += 1
        if res[1] == 0:
            res[1] = check
        
        return res