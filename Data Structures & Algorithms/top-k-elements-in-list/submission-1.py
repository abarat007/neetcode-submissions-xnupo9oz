class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        nums_map = {}
        for num in nums:
            nums_map[num] = 1 + nums_map.get(num, 0)
        
        nums_heap = []
        for val, freq in nums_map.items():
            nums_heap.append((freq, val))
        
        heapq.heapify_max(nums_heap)

        while k > 0:
            freq, val = heapq.heappop_max(nums_heap)
            res.append(val)
            k -= 1
        
        return res


        



        