class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def check(s):
            if len(s) < 2:
                return ""

            letters = set(s)
            for i in range(len(s)):
                if s[i].swapcase() not in letters:
                    s_left = check(s[:i])
                    s_right = check(s[i+1:])
                    return s_left if len(s_left) >= len(s_right) else s_right
                
            return s

        return check(s)