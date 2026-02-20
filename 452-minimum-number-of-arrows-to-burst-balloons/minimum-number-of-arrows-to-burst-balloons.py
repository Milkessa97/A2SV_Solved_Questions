class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        points.sort()
        count = 0
        for idx in range(1,len(points)):
            if points[idx][0] <= points[idx-1][1]:
                points[idx] = [max(points[idx][0],points[idx-1][0]), min(points[idx][1],points[idx-1][1])]   
            else:
                count+=1
            if idx == len(points)-1:
                    count+=1
        return count