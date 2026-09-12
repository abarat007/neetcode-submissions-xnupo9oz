class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for gap in range(2,n):
            for l in range(0, n-gap):
                r = l+gap
                candidate = 0
                for k in range(l+1, r):
                    candidate = max(candidate, dp[l][k] + nums[l] * nums[k] * nums[r]+ dp[k][r])
                    dp[l][r] = candidate
        
        return dp[0][n-1]
        

        