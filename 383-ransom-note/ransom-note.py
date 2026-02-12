class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_r = Counter(ransomNote)
        count_m = Counter(magazine)
        return count_r <= count_m