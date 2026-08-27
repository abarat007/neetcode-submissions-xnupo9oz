class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(s):
                res.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                curr = s[i:j+1]
                # if curr is a palindrome, add it to subset
                rev = curr[::-1]
                if curr == rev:
                    subset.append(curr)
                    dfs(j+1)
                    subset.pop()            
    
        dfs(0)
        return res


        