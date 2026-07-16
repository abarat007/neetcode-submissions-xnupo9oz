class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            # Check if r and c are out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            
            # if grid[r][c] == 0, we can skip it
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c-1)
            area += dfs(r,c+1)

            return area

        # Loop through the grid
        # dfs if its a 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(maxArea, area)
        
        return maxArea

        