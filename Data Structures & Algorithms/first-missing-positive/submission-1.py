class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # if the value is negative, ignore it
        # it should map to res[idx] = num - 1

        # For example,
        # res[0] = 1
        # res[1] = 2
        # res[2] = 3

        # nums = [3,4,-1,1]
        n = len(nums)
        # we swap the value in nums with its correct position
        # for example, nums[0] = 3. this value should actually be in nums[2], so we swap values when nums[i] != (i+1)
        idx = 0
        while idx < n:
            current_val = nums[idx] # 3

            # if the current # belongs in the array, and it's not in the right place, we swap
            if current_val >= 1 and current_val <= n and nums[current_val-1] != current_val:
                correct_idx = current_val - 1
                # swap those values
                nums[idx], nums[correct_idx] = nums[correct_idx], nums[idx]
            else:
                idx += 1
        
        # nums = [1, -1, 3, 4]

        # go through the refined nums array, and we return the value that doesn't match the mapping rule

        # Mapping rule: nums[idx] = idx + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1





        # Solution
        # s = set(nums)
        # x = 1
        # while x in s:
        #     x += 1
        # return x

        



        