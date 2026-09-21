class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # {2, 3, 4, 5, 10, 20}
        longest = 0

        for num in nums:
            # find the start of the sequence
            if num - 1 not in nums_set:
                current = num
                length = 1
                # now we'll loop and increment length
                while current + 1 in nums_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
            
            




        