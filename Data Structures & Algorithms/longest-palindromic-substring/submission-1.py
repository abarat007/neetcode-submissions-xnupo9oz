class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        def expand(left, right):
            nonlocal res
            curr = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr = s[left:right+1]
            
                if len(curr) > len(res):
                    res = curr
                
                left -= 1
                right += 1
        
        for idx in range(len(s)):
            # odd length 's'
            expand(idx, idx)

            # even length 's'
            expand(idx, idx+1)    

        return res    




        


        

        

        
        