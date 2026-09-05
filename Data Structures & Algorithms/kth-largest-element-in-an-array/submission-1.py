class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_heap = nums.copy()
        heapq.heapify_max(nums_heap)
        res = 0

        while k > 0:
            res = heapq.heappop_max(nums_heap)
            k -= 1
        
        return res
        
        
