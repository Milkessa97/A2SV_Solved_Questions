class Solution:
    def romanToInt(self, s: str) -> int:
        mydict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        mylist = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        output = 0
        for x in range(len(s)-1):
            output += mydict[s[x]]
            if mydict[s[x]] < mydict[s[x+1]]:
                output -= 2*mydict[s[x]]
        output += mydict[s[-1]]
        return output

