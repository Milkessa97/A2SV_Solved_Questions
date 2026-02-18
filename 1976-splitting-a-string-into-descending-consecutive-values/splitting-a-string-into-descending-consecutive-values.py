class Solution:
    def splitString(self, s: str) -> bool:
        res=[]
        def backtrack(i=0):
            # if int(s[:i])-int(s[i:]) != 1:
            #     return False
            if i >= len(s) and len(res) >= 2:
                return True
            for idx in range(i,len(s)):
                if not res or int(res[-1]) - int(s[i:idx+1]) == 1:
                    res.append(s[i:idx+1])
                    if backtrack(idx+1):
                        return True
                    res.pop()
                
            return False
        return backtrack()


