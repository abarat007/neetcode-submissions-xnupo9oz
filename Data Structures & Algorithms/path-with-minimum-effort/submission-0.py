class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])


        visited = set()
        min_heap = [(0,0,0)] # (effort to cell, r, c)
        directions = [[1,0], [-1,0], [0,1], [0,-1]] # down, up, right, left
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)
            if (r,c) in visited:
                continue
            
            visited.add((r,c))

            if r == rows - 1 and c == cols - 1:
                return effort
            
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if (new_r, new_c) not in visited:
                        distance = abs(heights[r][c] - heights[new_r][new_c])

                        new_effort = max(effort, distance)

                        heapq.heappush(min_heap, (new_effort, new_r, new_c))
            
        return 0



        
            
            
            

            


        
        



        
        