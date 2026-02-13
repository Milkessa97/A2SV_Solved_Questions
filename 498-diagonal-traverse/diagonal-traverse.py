class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)-1
        n = len(mat[0])-1
        res = []
        i, j = 0, 0
        if len(mat) == 1:
            return mat[0]
        while i < m or j < n:
            while i > 0 and j < n:
                res.append(mat[i][j])
                i -= 1
                j += 1
            res.append(mat[i][j])
            if j < n:
                j += 1
            else:
                i += 1
            if i == m and j == n:
                res.append(mat[i][j])
                break
            while j > 0 and i < m:
                res.append(mat[i][j])
                i += 1
                j -= 1
            res.append(mat[i][j])
            if i < m:
                i += 1
            else:
                j += 1
            if i == m and j == n:
                res.append(mat[i][j])
                break
        return res
