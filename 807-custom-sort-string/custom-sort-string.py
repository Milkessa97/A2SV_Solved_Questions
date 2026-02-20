class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = [x for x in s.strip()]
        compare = defaultdict(int)
        val = 1

        for char in order:
            compare[char] = val
            val += 1

        chars.sort(key=lambda x: compare[x])

        return ''.join(chars)