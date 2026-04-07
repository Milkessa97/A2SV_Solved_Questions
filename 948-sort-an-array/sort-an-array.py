class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(leftSide,rightSide):
            res = []
            p1,p2 =0,0
            while p1 < len(leftSide) and p2 < len(rightSide):
                if leftSide[p1] < rightSide[p2]:
                    res.append(leftSide[p1])
                    p1 += 1
                else:
                    res.append(rightSide[p2])
                    p2 += 1
            res.extend(leftSide[p1:])
            res.extend(rightSide[p2:])
            
            return res
        
        def mergeSort(left,right,arr):
            if left == right:
                return [arr[left]]
            mid = (left+right)//2

            left = mergeSort(left,mid,arr)
            right = mergeSort(mid+1,right,arr)

            return merge(left,right)

        return mergeSort(0,len(nums)-1,nums)