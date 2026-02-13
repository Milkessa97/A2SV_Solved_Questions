class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        flag = False
        buffer = ""
        for line in source:
            idx = 0
            while idx < len(line):
                if not flag and idx+1 < len(line) and line[idx]+line[idx+1] == "//":
                    break
                elif not flag and idx+1 < len(line) and  line[idx]+line[idx+1] == "/*":
                    flag = True
                    idx += 2
                elif flag and idx+1 < len(line) and line[idx]+line[idx+1] == "*/":
                    flag=False
                    idx += 2
                elif not flag:
                    buffer += line[idx]
                    idx += 1
                else:
                    idx += 1
            if not flag and buffer:
                res.append(buffer)
                buffer = ""
        return res
