class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        print(nums_set)
        # {2, 3, 4, 5, 10, 20}

        max_len = 0

        for num in nums_set:
            if num -1 not in nums_set:
                curr_num = num # 2
                curr_len = 1
                while curr_num + 1 in nums_set:
                    curr_len += 1
                    curr_num += 1
            
                max_len = max(max_len, curr_len)
        
        return max_len

        