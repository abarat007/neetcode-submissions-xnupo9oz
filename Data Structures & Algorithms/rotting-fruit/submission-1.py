class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        time = 0

        queue = deque()

        # Count fresh oranges and store rotten oranges into queue for bfs
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r,c])

        def bfs(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            if grid[r][c] == 1:
                grid[r][c] = 2
                fresh -= 1
                queue.append([r, c])


        directions = [[1,0],[-1,0],[0,1],[0,-1]] 
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    bfs(new_r, new_c)
                    # if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols or grid[new_r][new_c] == 0:
                    #     continue
                    # if grid[new_r][new_c] == 1:
                    #     grid[new_r][new_c] = 2
                    #     fresh -= 1
                    #     queue.append([new_r, new_c])
                
            time += 1
        
        return time if fresh == 0 else -1
        

        

        