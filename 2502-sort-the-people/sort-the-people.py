class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        if len(names) == 1:
            return names
        for i in range(len(names)-1):
            left, right = 0, 1
            while right < len(names):
                if heights[right] > heights[left]:
                    names[right], names[left] = names[left], names[right]
                    heights[right], heights[left] = heights[left], heights[right]
                right += 1
                left += 1
        return names

