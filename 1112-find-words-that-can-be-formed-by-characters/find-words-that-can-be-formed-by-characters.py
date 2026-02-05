class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            count = Counter(chars)
            for char in word:
                if char in count:
                    count[char] -= 1
                    if count[char] == 0:
                        del count[char]
                else:
                    break
            else:
                res += len(word)
        return res

