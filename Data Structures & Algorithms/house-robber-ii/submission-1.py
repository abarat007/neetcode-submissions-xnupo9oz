class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_one(arr):
            dp = {}

            def dfs(idx):
                if idx >= len(arr):
                    return 0
                
                if idx in dp:
                    return dp[idx]

                dp[idx] = max(arr[idx]+dfs(idx+2), dfs(idx+1))
                return dp[idx]
            return dfs(0)
        # Recurrence Relation
        # dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
        return max(rob_one(nums[1:]), rob_one(nums[:-1]))