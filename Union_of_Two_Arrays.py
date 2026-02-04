class Solution:    
    def findUnion(self, a, b):
        # code here
        a.extend(b)
        c= set(a)
        res = [ x for x in c]
        return res
