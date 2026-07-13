class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        # candidates = [1, 2, 2, 4, 5, 6, 9]
        # target = 8

        res = []
        subset = []

        def dfs(idx, remaining):
            if remaining == 0:
                res.append(subset.copy())
                return
            if remaining < 0 or idx >= len(candidates):
                return
            
            # Choice 1: we add candidates[idx] and dfs idx + 1
            subset.append(candidates[idx])
            
            dfs(idx + 1, remaining - candidates[idx])

            # Set up choice 2
            subset.pop()

            # Choice 2: we skip it
            # We need to find an idx that isn't the same as the current idx
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, remaining)
        
        dfs(0, target)
        return res
        