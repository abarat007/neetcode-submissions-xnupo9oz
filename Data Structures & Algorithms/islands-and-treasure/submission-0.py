class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        queue = deque()

        # Store all the treasure coordinates into the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])

        distance = 1
        # Loop through all the treaure coordinates in the queue, and run bfs to change value
        while queue:
            size = len(queue)
            while size > 0:
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    # Alter cell if its valid location and 2147483647
                    if new_r >= 0 and new_c >= 0 and new_r < rows and new_c < cols and grid[new_r][new_c] == 2147483647:
                        grid[new_r][new_c] = distance
                        queue.append([new_r,new_c])
                size -= 1
            distance += 1
                

        

        


        