class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False
        
        rows = n1 + 1
        cols = n2 + 1

        dp = [[False for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = True 

        # dp[r][c] = using first r letters in s1 and first c letters in s2
        # can we make the first (r+c) letters in s3? (True/False)

        for r in range(rows):
            for c in range(cols):
            # if the last char came from s1 and it matches the same idx in s3
                if r > 0 and dp[r-1][c] and s1[r-1] == s3[r+c-1]:
                    dp[r][c] = True
            # if the last char came from s2 and it matches the same idx in s3
                if c > 0 and dp[r][c-1] and s2[c-1] == s3[r+c-1]:
                    dp[r][c] = True
        return dp[n1][n2]
                



        