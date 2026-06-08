class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {1:1,2:2,3:3}
        # store tuples in max_heap (frequency:val) with heapq.heapify_max(max_heap)
        # heapq.heappop while k > 0 and store freq back into a res array
        # k -= 1

        res = []
        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        
        max_heap = [(val, key) for key, val in nums_map.items()]
        # (freq, val)
        heapq.heapify_max(max_heap)

        while k > 0:
            freq, val = heapq.heappop_max(max_heap)
            res.append(val)
            k -= 1
        
        return res



        