class Solution:
    def maxArea(self, heights: List[int]) -> int:
        base_length = 0
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            base_length = right - left
            area = min(heights[left], heights[right]) * base_length
            maxArea = max(area, maxArea)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -=1 
        
        return maxArea


        