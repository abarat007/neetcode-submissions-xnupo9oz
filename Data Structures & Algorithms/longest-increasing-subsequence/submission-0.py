class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        max_len = 0

        def dfs(idx):
            if idx in dp:
                return dp[idx]
            
            best = 1

            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    best = max(best, 1 + dfs(i))
            
            dp[idx] = best
            return dp[idx]
        
        for i in range(len(nums)):
            max_len = max(max_len, dfs(i))
        
        return max_len
        
            
            
            
            
        
        