class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_window_len = float('inf')
        left = 0
        window_sum = 0

        for right in range(n):
            window_sum += nums[right]
            while window_sum >= target:
                min_window_len = min(min_window_len, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return min_window_len if min_window_len != float('inf') else 0


        
        
        






            
        