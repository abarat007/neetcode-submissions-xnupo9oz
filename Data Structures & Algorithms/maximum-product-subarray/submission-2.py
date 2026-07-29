class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]

        for i in range(1, len(nums)):
            num = nums[i] # 4
            temp_max = max_prod # 2

            max_prod = max(num, num * temp_max, num * min_prod)
            min_prod = min(num, num * temp_max, num * min_prod)

            global_max = max(global_max, max_prod)
        
        return global_max

        
        