class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        memo = [[-1] * n for _ in range(m)]
        print(memo)

        def dfs(r,c):
            # We have reached the goal
            if r == m - 1 and c == n - 1:
                return 1
            
            # if we try to traverse out of bounds, return
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            
            if memo[r][c] != -1:
                return memo[r][c]
            
            # dfs right and down
            memo[r][c] = dfs(r,c+1) + dfs(r+1,c)
            return memo[r][c]
            

        return dfs(0,0)


        


        