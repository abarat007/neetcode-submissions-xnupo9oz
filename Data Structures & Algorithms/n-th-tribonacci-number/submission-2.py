class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0:0, 1:1, 2:1}
        # recurrence relation:
        # for n > 2, res = dfs(x) for x in range(x-1, -1, -1)
        def dfs(x):
            if x <= 2:
                return memo[x]
            if x in memo:
                return memo[x]
            
            memo[x] = dfs(x-1) + dfs(x-2) + dfs(x-3)
            return memo[x]
        
        return dfs(n)
        
        
        



        


        