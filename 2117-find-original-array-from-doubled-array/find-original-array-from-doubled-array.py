class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        if count[0] % 2 == 1:
            return []
        for key in sorted(count):
            if count[key] > count[key*2]:
                return []
            if key != 0:
                count[key*2] -= count[key]
            else:
                count[key] = int(count[key]/2)
        return list(count.elements())