class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i_idx = set()
        j_idx = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    i_idx.add(i)
                    j_idx.add(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in i_idx or j in j_idx:
                    matrix[i][j] = 0