class Solution:
    def isValid(self, s: str) -> bool:
        #declare pairs of valid parenthesis
        validPairs={"}":"{",")":"(","]":"["}
        stack=[]

        for char in s:
            if stack:
                #remove the last element if a pair is found else append the latest element
                if char in validPairs and validPairs[char]==stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                #just append if stack is empty
                stack.append(char)

        #check and return if any element is left in the stack
        return not stack