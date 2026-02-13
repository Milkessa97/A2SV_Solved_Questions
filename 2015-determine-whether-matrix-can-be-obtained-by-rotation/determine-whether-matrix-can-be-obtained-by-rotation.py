class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if mat == target:
                return True
            mat = self.rotateRight(mat)
        return False
    
    def rotateRight(self, mat: List[List[int]]):
        for i in range(len(mat)):
            for j in range(len(mat)):
                if j > i:
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        for row in mat:
            row.reverse()
        return mat