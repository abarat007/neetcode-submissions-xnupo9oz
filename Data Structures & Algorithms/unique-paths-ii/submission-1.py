class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0

        memo = [[-1] * cols for _ in range(rows)]

        def dfs(r,c):
            # if we reach the bottom-right, return 1
            if r == rows - 1 and c == cols - 1:
                return 1
            
            # If we go out of bounds, return 0
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            
            # If a position is in memo, return it
            if memo[r][c] != -1:
                return memo[r][c]
            
            # if the position is an obstacle, return 0
            if obstacleGrid[r][c] == 1:
                return 0
            
            # Traverse right and down
            memo[r][c] = dfs(r, c+1) + dfs(r+1,c)
            return memo[r][c]
        
        return dfs(0,0)