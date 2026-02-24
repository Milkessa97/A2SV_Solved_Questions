class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        check=Counter(s)
        res=''
        for word in dictionary:
            word_c = Counter(word)
            if word_c <= check:
                p = 0
                for char in s:
                    if char == word[p]:
                        p+=1
                    if p == len(word):
                        if len(word) == len(res):
                            res = min(res,word)
                        elif len(word) > len(res):
                            res = word
                        break
        return res
                