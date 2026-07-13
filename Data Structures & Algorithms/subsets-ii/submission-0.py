class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        def dfs(idx):
            if idx == len(nums):
                res.append(subset.copy())
                return
            
            # Choice 1: add value
            subset.append(nums[idx])
            dfs(idx + 1)

            # Set up choice 2 by popping to set up the other path
            subset.pop()
            # Choice 2: 
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1 
            dfs(idx + 1)
        

        dfs(0)
        return res


        