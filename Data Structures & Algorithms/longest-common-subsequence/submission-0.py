class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if they're both the same, return the length of either one
        if text1 == text2:
            return len(text1)
        # We can only make a valid subsequence by breaking the smaller text into the larger text
        n = len(text1) # rows
        m = len(text2) # cols
 
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # print(dp)
        # [0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0, 0]
        
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        return dp[0][0]


        

        
        