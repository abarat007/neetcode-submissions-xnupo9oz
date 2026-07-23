class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        best_start = 0
        best_len = 0
        def expand(left, right):
            nonlocal res
            nonlocal best_start
            nonlocal best_len
            curr = ""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # curr = s[left:right+1]
                curr_len = right - left + 1

                if curr_len > best_len:
                    best_start = left
                    best_len = curr_len
                
                left -= 1
                right += 1
        
        for idx in range(len(s)):
            # odd length 's'
            expand(idx, idx)

            # even length 's'
            expand(idx, idx+1)    

        return s[best_start:best_start + best_len] 




        


        

        

        
        