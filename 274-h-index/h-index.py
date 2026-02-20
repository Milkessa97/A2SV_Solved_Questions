class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for idx in range(len(citations)):
            h = len(citations) - idx
            if citations[idx] >= h:
                return h
        return 0
