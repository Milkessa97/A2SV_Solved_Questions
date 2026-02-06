class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        common = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word.strip()))
            common[key].append(word)
        return [x for x in common.values()]