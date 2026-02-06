class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common = Counter(nums).most_common()
        res = []
        for i in range(0,k):
            res.append(most_common[i][0])
        return res