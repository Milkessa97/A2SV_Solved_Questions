class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        valids = []
        curr = ""
        def backtrack(idx):
            nonlocal valids,curr
            if idx == n:
                valids.append(curr)
                return
            if curr[-1] != 'a':
                curr += 'a'
                backtrack(idx+1)
                curr = curr[:-1]

            if curr[-1] != 'b':
                curr += 'b'
                backtrack(idx+1)
                curr = curr[:-1]
            
            if curr[-1] != 'c':
                curr += 'c'
                backtrack(idx+1)
                curr = curr[:-1]
        
        for char in ['a','b','c']:
            curr += char
            backtrack(1)
            curr = curr[:-1]
        
        if k <= len(valids):
            return valids[k-1]
        return ''