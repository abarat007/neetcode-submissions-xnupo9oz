class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)
        

        def dfs():
            # This means that we have finished building a subset
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
            
                # Choice 1: use nums[i]
                subset.append(nums[i])
                used[i] = True

                dfs()

                # Undo after done exploring
                subset.pop()
                used[i] = False
            

        dfs()
        return res