class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        n = len(nums)
        count = 0

        prefix_sums = {0:1} # we've seen the prefix sum 0 1 time


        for num in nums:
            pre_sum += num

            if pre_sum - k in prefix_sums:
                count += prefix_sums[pre_sum - k]
            
            # add pre_sum to prefix_sums map
            if pre_sum in prefix_sums:
                prefix_sums[pre_sum] += 1
            else:
                prefix_sums[pre_sum] = 1
        
        return count
            




        