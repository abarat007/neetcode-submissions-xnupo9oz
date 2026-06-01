class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_array = [1] * n
        suff_array = [1] * n
        res = [0] * n
        # Build a prefix product array
        for i in range(1, n):
            pref_array[i] = nums[i - 1] * pref_array[i - 1]
         
        # Build a suffix product array
        for j in range(n - 2, -1, -1):
            suff_array[j] = nums[j + 1] * suff_array[j + 1]
        
        # Multiply each idx in prefix + suffix array and append to res
        for i in range(len(nums)):
            res[i] = pref_array[i] * suff_array[i]
        
        return res

        