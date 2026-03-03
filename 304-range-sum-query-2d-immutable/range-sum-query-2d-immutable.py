class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.pref = [[0 for _ in range(m+1)] for j in range(n+1)]
        for i in range(n):
            for j in range(m):
                self.pref[i][j] = matrix[i][j] + self.pref[i-1][j] + self.pref[i][j-1] - self.pref[i-1][j-1]
        print(self.pref)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        union = self.pref[row2][col2]
        left_sub = self.pref[row2][col1-1]
        top_sub = self.pref[row1-1][col2]
        inter = self.pref[row1-1][col1-1]
        return union - left_sub - top_sub + inter
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)