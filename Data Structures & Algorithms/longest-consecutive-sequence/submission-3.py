class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        nums_map = {}
        # Move array elements into dictionary
        for num in nums:
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        res = []
        for val in nums_map:
            counter = 1
            next_val = val + 1
            if val - 1 not in nums_map:
                while next_val in nums_map:
                    counter += 1
                    next_val += 1
                res.append(counter)
        
        return max(res)

        
        