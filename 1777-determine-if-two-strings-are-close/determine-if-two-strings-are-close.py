class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1 = Counter(word1)
        w2 = Counter(word2)

        letter1 = set(w1.keys())
        letter2 = set(w2.keys())

        w1 = sorted(w1.values())
        w2 = sorted(w2.values())

        return w1 == w2 and letter1 == letter2  
                