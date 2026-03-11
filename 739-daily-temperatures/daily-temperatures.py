class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0]*len(temperatures)
        for idx,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                popped, _ = stack.pop()
                res[popped] = idx-popped
            stack.append([idx,temp])
        return res