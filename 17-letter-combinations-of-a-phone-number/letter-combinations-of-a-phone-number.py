class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pairs = {"2":"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        res = []
        def exploit(dig,curr = ""):
            if not dig:
                res.append(curr)
                return
            for values in pairs[dig[0]]:
                for char in values:
                    curr += char
                    exploit(dig[1:],curr)
                    curr = curr[:-1]
        
        exploit(digits,"")

        return res

        
        
