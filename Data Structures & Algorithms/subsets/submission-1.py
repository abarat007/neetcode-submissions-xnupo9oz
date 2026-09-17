class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # subset = [] # exclude 1
        # subset = [2]# include 2
        # subset = [1] # include 1
        # etc. etc.

        # nums = [1,2,3]
        # [], [1], [2], [3], [1,2], [2,3], [1,3], [1,2,3]

        n = len(nums)

        # subset = [1]
        def backtrack(idx):
            # stopping the backtracking
            if idx == n:
                res.append(subset[:])
                return
            
            # Include nums[i]
            subset.append(nums[idx])
            backtrack(idx + 1)

            # Exclude nums[i]
            subset.pop()
            backtrack(idx + 1)


        backtrack(0)
        return res

        