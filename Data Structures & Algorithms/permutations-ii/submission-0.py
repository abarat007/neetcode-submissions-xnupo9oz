class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        used = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # If this number is a duplicate, only use it after the previous duplicate has been used
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Choice 1: use the number
                subset.append(nums[i])
                used[i] = True

                dfs()

                # Choice 2: use the next number
                subset.pop()
                used[i] = False

        dfs()
        return res
        