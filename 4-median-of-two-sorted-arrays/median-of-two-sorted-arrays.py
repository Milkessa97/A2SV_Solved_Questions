class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def mergeSort(nums1,nums2):
            res = []
            p1,p2 = 0,0
            while p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    res.append(nums1[p1])
                    p1 += 1
                else:
                    res.append(nums2[p2])
                    p2+=1
            res.extend(nums1[p1:])
            res.extend(nums2[p2:])
            return res

        new_list = mergeSort(nums1,nums2)
        p = len(new_list)//2
        if len(new_list) % 2 == 0:
            return (new_list[p] + new_list[p-1])/2
        return new_list[p]