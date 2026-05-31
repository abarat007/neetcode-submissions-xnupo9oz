class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We need to use a min heap because we want the lowerst distances from the origin to be returned

        res = []
        min_heap = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            min_heap.append([distance, x, y])
        
        # Convert the min_heap list into a heap 
        heapq.heapify(min_heap)

        # Get the k smallest distances from the heap and add it to the resulting array
        while k > 0:
            distance, x, y = heapq.heappop(min_heap)
            res.append([x, y])
            k -= 1
        
        return res
        