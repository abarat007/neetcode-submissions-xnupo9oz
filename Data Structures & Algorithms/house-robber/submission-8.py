
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(idx):
            if idx >= len(nums):
                return 0
            
            if idx in dp:
                return dp[idx]
            
            dp[idx] = max(nums[idx]+dfs(idx+2), dfs(idx+1))
            return dp[idx]

        
        return dfs(0)
        

        
        