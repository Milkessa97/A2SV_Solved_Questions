class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        sentence = ""
        def backtrack(i,curr=""):
            nonlocal res,sentence
            if i == len(s):
                if sentence and ''.join(sentence.split()) == s:
                    res.append(sentence[:-1])
                return True
            
            curr += s[i]
            if curr in wordDict:
                sentence += curr+' '
                backtrack(i+1,'')
                sentence = sentence[:-(len(curr)+1)]

            backtrack(i+1,curr)
        backtrack(0,'')
        return res