class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ptn = list(pattern.strip())
        s = list(s.split())
        check_ptn = defaultdict(str)
        check_s = defaultdict(str)
        p = 0
        if len(ptn) != len(s):
            return False
        while p < len(ptn):
            if ptn[p] not in check_ptn:
                if s[p] not in check_s:
                    check_ptn[ptn[p]] = s[p]
                    check_s[s[p]] = ptn[p]
                else:
                    return False
            else:
                word = check_s[s[p]]
                if word != ptn[p]:
                    return False
            p+=1
        return True 
