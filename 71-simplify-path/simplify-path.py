class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [dir for dir in path.split('/')]
        print(path)
        stack = []
        for dir in path:
            if dir == "." or dir == "":
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/'+'/'.join(stack)