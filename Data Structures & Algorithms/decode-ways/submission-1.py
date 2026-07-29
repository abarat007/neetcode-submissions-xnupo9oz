class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {} # {idx: val}
        # Valid only between 1-26 inclusive

        # Recurrence relation: dfs(i+1) + dfs(i+2)
        # digit 1: 1 <= d1 <= 2
        # digit 2: if d1 == '1': 0 <= d2 <= 9 else 0 <= d2 <= 6

        def dfs(idx):
            if idx >= len(s):
                return 1
            
            if idx in dp:
                return dp[idx]

            if s[idx] == '0':
                return 0
            
            ways = dfs(idx + 1)
            
            if idx + 1 < len(s) and 10 <= int(s[idx:idx+2]) <= 26:
                ways += dfs(idx + 2)
            
            dp[idx] = ways
            return ways
    
        return dfs(0)
        
        

        
            


        

        
        


        