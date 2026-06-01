class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if only 1 stone
        if len(stones) == 1:
            return stones[0]
        
        # We should use max heap because for each iteration we go by the 2 "heaviest" stone weights
        max_heap = []
        for stone in stones:
            max_heap.append(stone)
        
        # max heapify the max_heap array
        heapq.heapify_max(max_heap)

        
        # the simulation continues until the heap length is 1
        while len(max_heap) > 1:
            x = heapq.heappop_max(max_heap) # 2
            y = heapq.heappop_max(max_heap) # 2
            
            if x < y or y < x:
                heapq.heappush_max(max_heap, abs(y - x))
            
        if max_heap:
            return heapq.heappop_max(max_heap)
        else:
            return 0
            
            
        





        