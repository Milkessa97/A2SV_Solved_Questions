class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)-1
        max_h = 0

        while left <= right:
            md = (left+right)//2

            if citations[md] >= len(citations) - md:
                max_h = len(citations) - md
                right = md - 1
            else:
                left = md + 1
                
        return max_h