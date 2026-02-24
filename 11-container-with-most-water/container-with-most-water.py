class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height) - 1
        mx = 0
        
        while left < right:
            size = min(height[left],height[right]) * (right-left)
            mx = max(mx,size)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mx