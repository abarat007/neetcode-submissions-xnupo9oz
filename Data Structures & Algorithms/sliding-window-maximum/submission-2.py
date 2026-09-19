class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [] # we store (value, index)

        [1,2,1,0,4,2,6]
        # max_heap = [(1,0), (2,1), (1,1), etc...]

        res = []

        for idx, val in enumerate(nums):
            heapq.heappush_max(max_heap, (val, idx))

            # we should then remove all the elements that are outside the window
            while max_heap[0][1] <= idx - k:
                heapq.heappop_max(max_heap)
            
            # We append value to result if the index >= window size
            if idx >= k - 1:
                res.append(max_heap[0][0])
        
        return res



        

        