from collections import Counter
#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)

        return count_b <= count_a
