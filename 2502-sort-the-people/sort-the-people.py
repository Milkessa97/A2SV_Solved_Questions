class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_height = max(heights)+1
        counter=[[] for i in range(max_height)]
        for i in range(len(names)):
            counter[heights[i]].append(names[i])
        counter.reverse()
        res=[]
        for col in counter:
            res.extend(col)
        return res