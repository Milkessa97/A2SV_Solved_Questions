class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0]*len(temperatures)
        for idx,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = idx-popped
            stack.append(idx)
        return res