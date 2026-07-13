class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(idx, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            
            if remaining < 0 or idx >= len(nums):
                return
            
            # Choice 1: include nums[idx]
            subset.append(nums[idx])
            dfs(idx, remaining - nums[idx])

            # Set up choice 2
            subset.pop()

            # Choice 2: skip it and move to next number
            dfs(idx + 1, remaining)
        dfs(0, target)
        return res


        
