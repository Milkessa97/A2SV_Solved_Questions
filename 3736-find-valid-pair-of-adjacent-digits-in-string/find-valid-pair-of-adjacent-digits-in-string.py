class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        left, right = 0, 1
        while right<len(s):
            if count[s[left]] == int(s[left]) and count[s[right]] == int(s[right]) and s[left] != s[right]:
                return s[left]+s[right]
            left += 1
            right += 1
        return ""