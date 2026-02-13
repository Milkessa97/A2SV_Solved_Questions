class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        k = len(matrix[0])-1
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            res.append(row)
        return res