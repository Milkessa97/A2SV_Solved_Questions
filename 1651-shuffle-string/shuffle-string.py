class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        map_idx = defaultdict(str)

        for idx in range(len(indices)):
            map_idx[indices[idx]] = s[idx]
            
        return "".join(map_idx[x] for x in range(len(indices)))