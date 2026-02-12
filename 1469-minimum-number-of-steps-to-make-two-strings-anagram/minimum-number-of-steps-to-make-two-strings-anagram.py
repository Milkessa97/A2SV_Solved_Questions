class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        count = 0

        for key in count_s.keys():
            if key in count_t:
                if count_s[key] - count_t[key] > 0:
                    count += count_s[key] - count_t[key]
            else:
                count += count_s[key]

        return count