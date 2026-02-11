class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        total = 0

        for num in nums:
            if num % 2 == 0:
                total += num

        for query in queries:
            if nums[query[1]] % 2 == 0:
                num = nums[query[1]]
                nums[query[1]] += query[0]
                if nums[query[1]] % 2 == 0:
                    total += query[0]
                else:
                    total -= num
            else:
                nums[query[1]] += query[0]
                if nums[query[1]] % 2 == 0:
                    total += nums[query[1]]

            res.append(total)

        return res