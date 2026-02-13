class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
        for i in range(len(image)):
            for j in range(len(image)):
                image[i][j] = image[i][j] ^ 1
        return image