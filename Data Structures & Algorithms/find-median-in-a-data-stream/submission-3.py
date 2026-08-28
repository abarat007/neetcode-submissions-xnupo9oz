class MedianFinder:

    def __init__(self):
        self.min_heap = [] # Store right half of values
        heapq.heapify(self.min_heap) # make min heap

        self.max_heap = [] # Store left half of values
        heapq.heapify_max(self.max_heap) # make max heap

        self.vals = [] # Store incoming values

        self.median = 0
        

    def addNum(self, num: int) -> None:
        self.vals.append(num)
        heapq.heappush_max(self.max_heap, num)

        while len(self.min_heap) <= len(self.max_heap):
            # Pop largest value from max_heap
            val_moved = heapq.heappop_max(self.max_heap)

            # Move it into min_heap
            heapq.heappush(self.min_heap, val_moved)

        # if len(min_heap) > len(max_heap), move the smallest from min_heap back to max
        if len(self.min_heap) > len(self.max_heap):
            num_moved = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, num_moved)


    def findMedian(self) -> float:
        if len(self.vals) == 1:
            return self.vals[0]

        if len(self.vals) % 2 == 0:
            self.median = float((self.max_heap[0] + self.min_heap[0]) / 2)
        else:
            self.median = float(self.max_heap[0])
        return self.median

        