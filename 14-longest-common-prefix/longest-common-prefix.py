class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        check = strs[0]
        for i in range(1,len(strs)):
            p = 0
            if not check or not strs[i]:
                return ""
            while strs[i][p] == check[p]:
                p += 1
                if p == len(check) or p == len(strs[i]):
                    break
            check = check[:p]
        return check
