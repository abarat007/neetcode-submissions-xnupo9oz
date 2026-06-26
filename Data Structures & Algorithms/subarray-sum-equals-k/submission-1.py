class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1 and k == nums[0]:
            return 1
        
        prefix_count = {0:1}
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            needed = prefix_sum - k

            if needed in prefix_count:
                res += prefix_count[needed]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return res

        

            
