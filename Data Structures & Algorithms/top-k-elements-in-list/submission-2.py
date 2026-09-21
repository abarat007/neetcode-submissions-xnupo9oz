class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {} # val:freq
        max_heap = [] #(freq, val)
        # store frequency of each number in nums
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        max_heap = [(freq, val)for val, freq in freq.items()]
        heapq.heapify_max(max_heap)

        # Loop k down to 0, popping everytime, extracting the value with highest freq everytime, and appending to result
        while k > 0:
            freq, val = heapq.heappop_max(max_heap)
            res.append(val)
            k -= 1
        
        return res
        