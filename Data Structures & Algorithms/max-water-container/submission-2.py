class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        base_width = 0
        maxArea = 0

        [1,7,2,5,4,7,3,6]
        while left < right:
            base_width = right - left
            maxArea = max((min(heights[left], heights[right])) * base_width, maxArea)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return maxArea
            






        