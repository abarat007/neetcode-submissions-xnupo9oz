class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, ocean_set):
            # Check if the pair is out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            # Check if its already in the set
            if (r,c) in ocean_set:
                return
            
            ocean_set.add((r,c))

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                # Check if those coordinates are valid, and check if that new cell if >= curr cell value
                # if so, traverse to it, and add the pair to the set
                if new_r >= 0 and new_c >= 0 and new_r < rows and new_c < cols and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, ocean_set)
        
        # loop through every column: (top_row,c) and (bot_row, c)
        for c in range(cols):
            dfs(0, c, pacific) # top row (pacific)
            dfs(rows-1, c, atlantic) # bottom row (atlantic)
        
        # loop through every row: (r, left_col) and (r, right_col)
        for r in range(rows):
            dfs(r, 0, pacific) # left row (pacific)
            dfs(r, cols-1, atlantic) # right row (atlantic)
    

        intersection = pacific & atlantic
        res = []
        for r,c in intersection:
            res.append([r,c])
        
        return res
        
        # Pacific Set: {(0, 1), (0, 4), (0, 0), (0, 3), (2, 0), (0, 2), (1, 0)}
        # Atlantic Set: {(2, 4), (0, 4), (2, 1), (2, 0), (1, 4), (2, 3), (2, 2)}

            
      

        

