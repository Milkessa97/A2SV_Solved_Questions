class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i+j == len(matrix)-1:
                    break
                n = len(matrix)-1
                matrix[i][j], matrix[n-j][n-i] = matrix[n-j][n-i], matrix[i][j]
        return matrix.reverse()

        


        