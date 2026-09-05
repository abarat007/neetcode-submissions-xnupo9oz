class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distance_heap = []
        for x, y in points:
            distance = (x**2) + (y**2)
            distance_heap.append([distance, x, y])
        
        heapq.heapify(distance_heap)

        while k > 0:
            dist, x,y = heapq.heappop(distance_heap)
            res.append([x,y])
            k -= 1
        
        return res
        