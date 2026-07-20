class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) # number of stairs
        memo = {}
        # recurrence relation:
        # cost[i] + min(dfs(i+1), dfs(i+2))

        def dfs(idx):
            if idx >= n:
                return 0
            
            if idx in memo:
                return memo[idx]
            
            memo[idx] = cost[idx] + min(dfs(idx+1), dfs(idx+2))
            return memo[idx]
        
        return min(dfs(0), dfs(1))
            
            




        
        