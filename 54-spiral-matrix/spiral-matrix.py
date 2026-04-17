class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        offset = 0
        res = []
        total_len = len(matrix) * len(matrix[0])
        
        for i in range(len(matrix)):

            for j in range(offset,len(matrix[i]) - offset):
                res.append(matrix[i][j])
                if len(res) == total_len:
                    return res

            for j in range(offset + 1,len(matrix) - offset):
                res.append(matrix[j][-1-offset])
                if len(res) == total_len:
                    return res

            for j in range(len(matrix[i]) - offset - 2, -1 + offset, -1):
                res.append(matrix[-1-offset][j])
                if len(res) == total_len:
                    return res

            for j in range(len(matrix) - offset - 2, offset , -1):
                res.append(matrix[j][offset])
                if len(res) == total_len:
                    return res

            offset += 1
        return res