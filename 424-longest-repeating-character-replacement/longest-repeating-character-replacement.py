class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        freq = Counter()
        max_len = 0
        max_freq = [0,""]

        while right < len(s):

            freq[s[right]] += 1
            if freq[s[right]] > max_freq[0]:
                max_freq[0] = freq[s[right]]
                max_freq[1] = s[right]

            while right-left-max_freq[0]+1 > k:
                freq[s[left]] -= 1
                for key,val in freq.items():
                    if val > max_freq[0]:
                        max_freq = [val,key]
                left += 1

            max_len = max(max_len,right-left+1)
            right+=1

        return max_len