class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mapping = {}

        for i in range(1, n+1):
            mapping[i] = []
        
        for time in times:
            src, dest, weight = time[0], time[1], time[2]
            mapping[src].append((weight,dest))
        
        min_heap = [(0, k)] # (time_to_node, k)
        visited = set()
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            visited.add(node)
            max_time = time
            for weight, dest in mapping[node]:
                if dest not in visited:
                    heapq.heappush(min_heap, (time + weight, dest))
        
        if len(visited) != n:
            return -1
        
        return max_time

        