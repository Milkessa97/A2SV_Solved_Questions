class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        check = []
        def recurse(p):
            nonlocal check
            if p == len(num):
                return len(check) > 2
                
            curr = ""
            for i in range(p,len(num)):
                curr += num[i]
                if len(curr) > 1 and curr[0] == '0':
                    break

                if len(check) >= 2:
                    if int(check[-1]) + int(check[-2]) == int(curr): 
                        check.append(curr)
                        if recurse(i+1):
                            return True
                        check.pop()
                else:
                    check.append(curr)
                    if recurse(i+1):
                            return True
                    check.pop()
               
            return False

        return recurse(0)


