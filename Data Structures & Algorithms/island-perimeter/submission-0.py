class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        # Directions
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # up, down, right, left
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                # Check if it is land
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 1:
                    # check all 4 directions
                    for dr, dc in directions:
                        new_r = r + dr
                        new_c = c + dc
                        # if out of bounds, perimeter++
                        if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                            perimeter += 1
                        # If the adjacent cell (left, right, up, down) is an island
                        elif grid[new_r][new_c] == 0:
                            perimeter += 1
                        else:
                            continue
        
        return perimeter

     

