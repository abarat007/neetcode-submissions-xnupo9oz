import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [[1,0], [-1,0], [0,1], [0,-1]] # down, up, right, left
        min_heap = [(grid[0][0],0,0)] # (time_needed_to_reach_cell, r,c)
        visited = set()

        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            if r == rows - 1 and c == cols - 1:
                return time
            
            if (r,c) in visited:
                continue
            
            visited.add((r,c))
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if (new_r, new_c) not in visited:
                        new_time = max(time, grid[new_r][new_c])
                        heapq.heappush(min_heap, (new_time, new_r, new_c))
        

            







        