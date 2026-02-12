class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        most_common = freq.most_common()
        res=""
        for char,char_freq in most_common:
            while char_freq != 0:
                res += char
                char_freq -= 1
        return res