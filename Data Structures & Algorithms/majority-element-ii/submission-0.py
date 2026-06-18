class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n // 3
        res = []

        nums_map = {}

        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        
        # {num:freq}
        for num, freq in nums_map.items():
            if freq > threshold:
                res.append(num)
        
        return res
