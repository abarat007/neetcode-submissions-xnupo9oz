class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use a min heap, because we want the smallest distances to x
        min_heap = []
        res = []
        # Store tuples in the heaps (distance, value)
        # That way, if the distance is equal, the min heap will still pop off the lowest based off of value

        for num in arr:
            pair = (abs(num - x), num)
            min_heap.append(pair)
        
        heapq.heapify(min_heap)

        # arr = [2,4,5,8], k = 2, x = 6
        # min_heap = [(4,6), (2,4), (1,5), (2,8)]

        while k > 0:
            distance, value = heapq.heappop(min_heap)
            res.append(value)
            k -= 1
        
        return sorted(res)


