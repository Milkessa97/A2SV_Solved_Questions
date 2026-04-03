class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = ""
        visited = set()

        def backtrack(p):
            nonlocal res,visited
            if len(res) == len(pattern) + 1:
                return True
            
            for i in range(1,10):
                if i not in visited:
                    visited.add(i)
                    
                    if pattern[p-1] == "I":
                        if i > int(res[-1]):
                            res += str(i)
                            if backtrack(p+1):
                                return True
                            res = res[:-1]
                    else:
                        if i < int(res[-1]):
                            res += str(i)
                            if backtrack(p+1):
                                return True
                            res = res[:-1]
                    visited.remove(i)

        for i in range(1,10):
            visited.add(i)
            res += str(i)
            if backtrack(1):  
                return res
            res = res[:-1]
            visited.remove(i)