class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        first = len(nums)-1
        perimeter = 0

        while first > 1:
            second = first-1
            third = second-1

            while third>=0:
                if nums[second]+nums[third] > nums[first]:
                    return nums[second]+nums[third]+nums[first]
                else:
                    second-=1
                    third-=1

            first-=1
            
        return 0