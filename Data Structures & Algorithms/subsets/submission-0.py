class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # nums = [1,2,3]
        subset = []
        def dfs(idx):
            if idx == len(nums):
                res.append(subset.copy())
                return
            
            # Choice 1: We add the value
            subset.append(nums[idx])
            dfs(idx + 1)

            # Undo Choice 1 (This is to set up the other path)
            # We are done exploring all subsets that include nums[idx].
            # Now remove nums[idx] so we can explore the path where nums[idx] is skipped.
            subset.pop()

            # Choice 2: We don't add the value (skip it)
            dfs(idx + 1)

        dfs(0)
        return res
            
            
            
            


        
        


        
        
        