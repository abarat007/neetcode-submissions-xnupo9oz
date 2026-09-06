class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0

        queue = deque()

        # store all the rotten oranges into the queue
        for r in range(rows):
            for c in range(cols):
                # add any rotten orange to the queue
                if grid[r][c] == 2:
                    queue.append([r,c])
                # Count how many fresh oranges are in the matrix
                if grid[r][c] == 1:
                    fresh += 1
        
        def bfs(r,c):
            nonlocal fresh
            # If we're trying to access a cell out of bounds, return nothing
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            
            # if cell is fresh fruit, rot it, add it to queue, and decrement fresh
            if grid[r][c] == 1:
                queue.append([r,c])
                grid[r][c] = 2
                fresh -= 1
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        # While the queue is valid, keep rotting oranges and appending to time
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    bfs(new_r, new_c)
            time += 1
        
        return time if fresh == 0 else -1





        

        

        