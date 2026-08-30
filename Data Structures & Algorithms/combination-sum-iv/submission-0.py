class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target+1)
        dp[0] = 1 # Only one way to get a sum of 0

        for curr in range(1, target + 1):
            for num in nums:
                if curr - num >= 0:
                    dp[curr] += dp[curr - num]
        return dp[target]


        