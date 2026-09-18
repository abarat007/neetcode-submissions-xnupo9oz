class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)

        # if there are 3 steps: [0,1,2]
        # dp[i] represents the # of ways to reach step i
        dp[1] = 1 # 1 way to go from step n to step n+1 (0->1)
        dp[2] = 2 # 2 ways to go from step n-1 to n+1(n-1 + 1 + 1, n-1 + 2)
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]







        