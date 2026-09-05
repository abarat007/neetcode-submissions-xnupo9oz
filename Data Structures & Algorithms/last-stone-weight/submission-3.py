class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        max_heap = stones.copy()
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop_max(max_heap) # 6
            y = heapq.heappop_max(max_heap) # 4
            if x < y or y < x:
                heapq.heappush_max(max_heap, abs(x-y))
        
        if max_heap:
            return heapq.heappop_max(max_heap)
        else:
            return 0




        