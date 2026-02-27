class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        check = set()
        left = 0
        res = []
        for right in range(len(s)):
            if check:
                check.add(s[right])
                count[s[right]] -= 1

                if count[s[right]] == 0:
                    del count[s[right]]
                    check.remove(s[right])
            else:
                check.add(s[right])
                count[s[right]] -= 1

                if count[s[right]] == 0:
                    del count[s[right]]
                    check.remove(s[right])

                if right-left:
                    res.append(right-left)
                left = right

        if len(s) - left:
            res.append(len(s) - left)
        return res
