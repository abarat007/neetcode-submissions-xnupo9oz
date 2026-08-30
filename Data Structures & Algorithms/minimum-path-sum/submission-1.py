class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # dp[r][c] represents the minimum cost from that cell to the bottom right cell in grid
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        # The bottom right cell is 0, because there is no sum to get to it, because it is the bottom right cell

        directions = [[0,1], [1,0]] # move right, down

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if r == rows - 1 and c == cols - 1:
                    # bottom right cell in dp = bottom right cell in grid
                    dp[r][c] = grid[r][c] 
                else:
                    min_neighbor_cost = float('inf')
                    for dr, dc in directions:
                        new_r = dr + r
                        new_c = dc + c
                        if new_r >= 0 and new_c >= 0 and new_r < rows and new_c < cols:
                            min_neighbor_cost = min(min_neighbor_cost, dp[new_r][new_c])
                        
                        dp[r][c] = grid[r][c]+ min_neighbor_cost
        return dp[0][0]