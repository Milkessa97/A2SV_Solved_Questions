class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        if len(names) == 1:
            return names
        
        left, right = 0, 1

        while left < len(names):
            max_idx = left

            while right < len(names):
                if heights[right] > heights[max_idx]:
                    max_idx = right
                right += 1

            names[left], names[max_idx] = names[max_idx], names[left]
            heights[left], heights[max_idx] = heights[max_idx], heights[left]

            left += 1
            right = left + 1

        return names