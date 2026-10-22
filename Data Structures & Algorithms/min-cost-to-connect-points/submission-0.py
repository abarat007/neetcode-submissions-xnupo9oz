class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        mapping = {i:[] for i in range(N)}

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                mapping[i].append((dist,j))
                mapping[j].append((dist,i))
        
        # 0: [(4, 1), (6, 2), (6, 3), (6, 4)], 
        # 1: [(4, 0), (2, 2), (2, 3), (2, 4)], 
        # 2: [(6, 0), (2, 1), (2, 3), (2, 4)], 
        # 3: [(6, 0), (2, 1), (2, 2), (4, 4)], 
        # 4: [(6, 0), (2, 1), (2, 2), (4, 3)]

        min_heap = [(0,0)] # cost, node
        visited = set()
        res = 0

        while len(visited) < N:
            cost, n = heapq.heappop(min_heap)
            if n in visited:
                continue
            res += cost
            visited.add(n)
            for weight, neighbor in mapping[n]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))
        
        return res
            


        