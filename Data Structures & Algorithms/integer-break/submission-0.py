class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        # loop from 2 to n, because 0 and 1 cannot be broken down further
        for i in range(2, n+1):
            # 
            for j in range(1, n+1):
                dp[i] = max(dp[i], j*(i-j), j * dp[i-j])
        
        return dp[n]





        