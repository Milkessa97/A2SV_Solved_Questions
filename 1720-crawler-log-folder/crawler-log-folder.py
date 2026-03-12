class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        for dir in logs:
            if dir[:2] == "..":
                if stack:
                    stack.pop()
            elif dir[:2] == "./":
                continue
            else:
                stack.append(dir)
        return len(stack)