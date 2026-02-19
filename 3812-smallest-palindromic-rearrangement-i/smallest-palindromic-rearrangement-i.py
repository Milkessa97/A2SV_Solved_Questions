class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)<=3:
            return s

        s = Counter(s)
        check=[]

        for key,val in s.items():
            check.append((key,val))
        check.sort()
        res = ''
        odd_letter = ''

        for x,y in check:
            if y%2==1:
                odd_letter=x

            rep = y//2
            while rep > 0:
                res+=x
                rep-=1

        if odd_letter:
            res+=odd_letter
            res+=res[:-1][::-1]
            
        else:
            res+=res[::-1]
        return res
    
                
