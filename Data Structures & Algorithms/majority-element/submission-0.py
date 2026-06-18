class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        threshold = n / 2

        majority = float('inf')

        nums_map = {}
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        
        for num, freq in nums_map.items():
            if freq > threshold:
                majority = num
        
        return majority


        