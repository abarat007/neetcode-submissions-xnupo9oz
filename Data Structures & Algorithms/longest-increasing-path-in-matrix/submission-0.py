class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_path = 0
        
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        directions = [[0,1], [0,-1], [1,0], [-1,0]] # right,left, down, up
        def dfs(r,c):
            if dp[r][c] != 0:
                return dp[r][c]
            
            best = 1

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if (0 <= new_r < rows and 0 <= new_c < cols and matrix[new_r][new_c] > matrix[r][c]):
                    best = max(best, 1 + dfs(new_r, new_c))
            dp[r][c] = best
            return dp[r][c]

        for r in range(rows):
            for c in range(cols):
                max_path = max(max_path, dfs(r,c))
        
        return max_path

                        

                
        

        

        