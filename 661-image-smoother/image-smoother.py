class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(img)):
            total=0
            count = 0
            line=[]
            for j in range(len(img[0])):
                if i > 0:
                    total += img[i-1][j]
                    count+=1
                    if j >0:
                        total += img[i-1][j-1]
                        count+=1
                    if j+1 < len(img[0]):
                        total += img[i-1][j+1]
                        count+=1

                if j >= 0:
                    total += img[i][j]
                    count+=1
                    if j>0:
                        total += img[i][j-1]
                        count+=1
                    if j+1 < len(img[0]):
                        total += img[i][j+1]
                        count+=1

                if i+1 <len(img):
                    total += img[i+1][j]
                    count+=1
                    if j >0:
                        total += img[i+1][j-1]
                        count+=1
                    if j+1 < len(img[0]):
                        total += img[i+1][j+1]
                        count+=1

                line.append(total//count)
                total = 0
                count=0

            res.append(line)
            
        return res